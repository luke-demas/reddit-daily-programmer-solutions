# r/dailyprogrammer
# challenge 2, difficult
# https://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/

# solution by Luke Demas

import time

def time_output(total):
    mins = total // 60
    sec = total % 60
    hours = mins // 60
    mins = mins % 60
    output = "Time Lapsed = {0:.0f}:{1:.0f}:{2:.0f}\n\n".format(int(hours), int(mins), sec)
    print(output)
    with open('log.txt', 'a') as log:
        log.write(output)

def lap_output(total):
    global count
    global stop
    count += 1
    mins = total // 60
    sec = total % 60
    hours = mins // 60
    mins = mins % 60
    output = "Lap {0} = {1:.0f}:{2:.0f}:{3:.0f}\n".format(int(count), int(hours), int(mins), sec)
    print(output)
    with open('log.txt', 'a') as log:
        log.write(output)
    if stop == False:
        stopwatch()

def stopwatch():
    global previous_lap
    global stop
    choice = input("Press Enter to stop, or l and Enter for lap.")
    if choice == 'l':
        lap = time.time()
        total = lap - previous_lap
        previous_lap = lap
        lap_output(total)
    else:
        stop = True
        end = time.time()
        total_lap = end - previous_lap
        lap_output(total_lap)
        total = end - start
        time_output(total)

stop = False
count = 0
input("Press Enter to start.")
start = time.time()
previous_lap = start
stopwatch()