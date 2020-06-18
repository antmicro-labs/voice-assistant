import time, sys

commands = ['VA:CMD:ON', 'VA:CMD:GO', 'VA:CMD:UP', 'VA:CMD:RIGHT', 'VA:CMD:STOP', 'VA:CMD:RIGHT', 'VA:CMD:ON', 'VA:CMD:GO', 'VA:CMD:NO', 'VA:CMD:RIGHT', 'VA:CMD:ON', 'VA:CMD:GO', 'VA:CMD:RIGHT', 'VA:CMD:ON', 'VA:CMD:GO']

i = 0
while i < len(commands):
    print(commands[i])
    sys.stdout.flush()
    #a little workaround for now:
    if i == 11:
        time.sleep(10)
    time.sleep(5)
    i += 1