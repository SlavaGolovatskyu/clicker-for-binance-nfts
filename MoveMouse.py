from datetime import datetime

from keyboard import is_pressed
from pyautogui import click

from active_ms_boxes import (
    parseActiveMysteryBoxList,
    getActiveMysteryBox
)

def move_mouse_to(coordinates: list) -> None:
    # checking if coords available
    # if not stoping script
    if not coordinates:
        print('Нету заданых координат. Останавливаем скрипт.')
        return 

    test = parseActiveMysteryBoxList(getActiveMysteryBox())

    if test:
        # old = int(datetime.now().timestamp() + 5)
        try:
            old = int(str(test[0]['Start'])[:10])
        except IndexError:
            print('На данный момент никаких нфт нету. Останавливаем скрипт.')
            return 
        
        new = int(datetime.now().timestamp())

        while new < old:
            if is_pressed('ctrl+k'):
                print('Скрипт успешно остановлен')
                return
            new = int(datetime.now().timestamp())
            print(int(old) - int(new), 'секунд осталось!')
        # cycle for all coords
        # function click() take 2 args 
        # x, y = width, height in px
        # after this she is move mouse to the coords which we have
        # and clicking on this coords
        len_coords = len(coordinates)
        while True:
            for index in range(0, len_coords, 2):
                if is_pressed('ctrl+k'):
                    print('Скрипт успешно остановлен')
                    return
                click(coordinates[index], coordinates[index+1])