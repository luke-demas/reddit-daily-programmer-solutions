# r/dailyprogrammer
# challenge 1, intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/

# solution by Luke Demas

# This function prints the current schedule to the user
def scheduleCheck(schedule):
    time = 0
    for item in range(len(schedule)):
        print(str(time) + " " + schedule[item])
        time = time + 1
    scheduleMenu()

# This function adds a specified event at a specified time
def scheduleAdd(schedule):
    time = input("When would you like to add an event?\n(0 - 23)\n")
    if int(time) < 0 or int(time) > 23:
        print("Invalid time\n")
        scheduleAdd(schedule)
    else:
        event = input("What is the event description?\n")
    schedule[int(time)] = event
    print("Event added!\n")
    scheduleMenu()

# This function deletes an event from the schedule
def scheduleDelete(schedule):
    time = input("What time would you like to clear?\n")
    schedule[int(time)] = "No event scheduled for this time!"
    print("Event deleted!\n")
    scheduleMenu()

# This function builds the menu
def scheduleMenu():
    choice = input("What would you like to do?\n(CHECK, ADD, DELETE, QUIT)\n")
    if choice == 'CHECK':
        scheduleCheck(schedule)
    elif choice == 'ADD':
        scheduleAdd(schedule)
    elif choice == 'DELETE':
        scheduleDelete(schedule)
    elif choice == 'QUIT':
        pass
    else:
        print("\nInvalid input.\n")
        scheduleMenu()

# This block of code initializes the schedule and prints the program's opening line
# The call to scheduleMenu starts the program
schedule = ["No event scheduled for this time!"]*24
print("Welcome to your event scheduler!\n")
scheduleMenu()