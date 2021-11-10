from pyautogui import size

from NoteMousePosition import note_mouse_position
from DataBaseEvents import DataBase

def get_users_coords():
    x = input('Координаты по оси x: ')
    y = input('Координаты по оси y: ')
    if x.isdigit() and y.isdigit():
        x, y = int(x), int(y)
        # receiving max size monitor's
        # x - width, y - height
        # function size() return tuple
        mon_x, mon_y = size()
        # checking if user's coordinates correct which belong him monitor's
        if x > mon_x or y > mon_y:
            print(("Вы указали неверные координаты. \n"),
                    ("Ваш монитор не поддерживает такие координаты. \n"),
                    (f"По ширине ваш монитор поддерживает координаты c: 0 по {mon_x} \n"),
                    (f"По высоте: 0 по {mon_y}."))
        else:
            note_mouse_position((x, y))
            print('Координаты успешно записаны.')
            print(DataBase().get_all_positions())
    else:
        print('Вместо цифр вы указали буквы или символы. Ну или минусовое число.')