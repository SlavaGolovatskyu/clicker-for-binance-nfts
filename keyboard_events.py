import requests as _req

from os import system
from keyboard import is_pressed
from pyautogui import position
from time import sleep

from colorama import (
    init,
    Fore
)

from NoteMousePosition import note_mouse_position
from MoveMouse import move_mouse_to
from additional_funcs import get_users_coords
from DataBaseEvents import DataBase

init()

__author__ = """SlavaGolovatskyu"""
__version__ = '1.4.1'

message = Fore.GREEN + f"""
AUTHOR: {__author__}
SCRIPT VERSION: {__version__}
[1] CTRL + L = LAUNCH SCRIPT
[2] CTRL + K = STOP SCRIPT (IF YOU WAS PRESSED CTRL + L)
[3] ALT + S = SAVED COORDINATES (YOU CAN SAVE SOME MANY COORDINATES)
[4] ALT + J = DELETE ALL COORDINATES WHICH WAS SAVED
[5] ALT + M = CLEAR MONITOR (ONLY IF YOU CAN'T LAUNCH SCRIPT)
[6] CTRL + O = PASTE YOUR COORDINATES WHICH YOU WANT
[7] CTRL + Q = QUIT FROM APP (IF SCRIPT NOT LAUNCHED)
[8] CTRL + X = DELETE LAST COORDINATES. FOR EXAMPLE [1, 2, 3, 4, 5, 6] => [1, 2, 3, 4]
[9] CTRL + I = SHOW ALL COORDINATES WHICH WAS SAVED.
"""

def key_events():
    # receiving coords from database and after this
    # using func move_mouse_to(coords)
    if is_pressed('ctrl+l'):
        print('Запущенно успешно.')
        coordinates = db.get_all_positions()
        move_mouse_to(coordinates)
        sleep(0.1)

    # adding mouse position
    elif is_pressed('alt+s'):
        note_mouse_position(position())
        print('Координаты записаны успешно')
        print(db.get_all_positions())
        sleep(0.1)

    # delete all saved mouse' positions
    elif is_pressed('alt+j'):
        db.clear_all_positions()
        print('Все позиции были успешно удалены.')
        sleep(0.1)
    
    #clear monitor
    elif is_pressed('alt+m'):
        system('cls')
        print(message)
        sleep(0.1)
    
    # user can note himself coords
    elif is_pressed('ctrl+o'):
        get_users_coords()
        sleep(0.1)

    # deleting last elem from db
    elif is_pressed('ctrl+x'):
        print(db.delete_last_elem())
        print(db.get_all_positions())
        sleep(0.1)

    # show all coords.
    elif is_pressed('ctrl+i'):
        print(db.get_all_positions())
        sleep(0.1)


def main():
    print(message)

    while True:
        if is_pressed('ctrl+q'):
            break
        key_events()


def is_permission(ip: str):
    url = f'https://slavik141.pythonanywhere.com/api/v1.0/users/find-by-ip/{ip}'
    find_user_by_ip = _req.get(url).json()

    if find_user_by_ip:
        main()
    else:
        print('У вас нету доступа к этой програме!')

try:
    ip = _req.get('https://api.ipify.org?format=json').json()['ip']
except:
    print('Нету подключения к интернету.')


if ip:
    #init database
    db = DataBase()
    db.create_table_if_not_ex()
    is_permission(ip)


