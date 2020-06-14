import time, sys

commands = ['VA:CMD:RIGHT', 'VA:CMD:RIGHT', 'VA:CMD:ON', 'VA:CMD:GO', 'VA:CMD:NO']

i = 0
while i < len(commands):
    print(commands[i])
    sys.stdout.flush()
    time.sleep(3)
    i += 1