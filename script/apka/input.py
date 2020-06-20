import time
import sys

commands = [('VA:CMD:ON', 3),
            ('VA:CMD:GO', 5),
            ('VA:CMD:UP', 5),
            ('VA:CMD:DOWN', 5),
            ('VA:CMD:RIGHT', 10),
            ('VA:CMD:STOP', 3),
            ('VA:CMD:RIGHT', 5),
            ('VA:CMD:ON', 5),
            ('VA:CMD:GO', 100)]

time.sleep(5)
for command in commands:
    print(command[0])
    sys.stdout.flush()
    time.sleep(command[1])
