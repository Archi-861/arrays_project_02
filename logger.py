from datetime import datetime
from os import stat

def log_action(name):
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    message = f'Perfoming {name} on array1 and array2 {time}'
    if stat('log_action.txt').st_size == 0:
        with open('log_action.txt', 'w') as file:
            file.write(message + '\n')
    else:
        with open('log_action.txt', 'a') as file:
            file.write(message + '\n')

