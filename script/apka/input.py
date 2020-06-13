import time, sys

commands = ['right', 'right', 'on', 'go', 'yes', 'yes', 'yes', 'no', 'go', 'left', 'left', 'go']

i = 0
while i < len(commands):
    print(commands[i])
    sys.stdout.flush()
    time.sleep(3)
    i += 1