# r/dailyprogrammer
# challenge 2, intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/

# solution by Luke Demas

# This function is the first path
# All invalid user input is handled via recursion
def introPath():
    choice = input("1 - ACCEPT MISSION\n2 - REFUSE\n")
    if choice == '1':
        print("You make your way to the gates of Ravenscreech Manor at nightfall.")
        print("Once there, you immediately feel a dark presence all around you.")
        print("You notice several entry points to the mansion.\n")
        entryPath()
    elif choice == '2':
        print("Are you sure about this?\n")
        rejectPath()

    else:
        print("Invalid input!\n")
        introPath()

# This function is a second path (1 of 2)
def rejectPath():
    choice = input("1 - I AM SURE\n2 - I'VE CHANGED MY MIND\n")
    if choice == '1':
        print("The vampires at Ravenscreech Manor grow in number and power.")
        print("In just 60 days the kingdom is destroyed.\n")
        print("GAME OVER.\n")
    elif choice == '2':
        introPath()

    else:
        print("Invalid input!\n")
        introPath()

# This function is a second path (2 of 2)
def entryPath():
    choice = input("1 - ENTER THROUGH THE FRONT DOOR\n2 - CHECK THE GARDENS\n3 - ENTER THROUGH THE BACK\n4 - CLIMB UP TO THE TERRACE\n")
    if choice == '1':
        print("You enter through the front door.")
        print("As it creaks open, hundreds of bat burst from the darkness")
        print("The bats surround you, you begin to suffocate\n")
        frontPath()
    elif choice == '2':
        print("You decide to check out the gardens.")
        print("It is beautiful, filled with sculptures and rose bushes.")
        print("You notice a young vampire child watching you.\n")
        gardensPath()
    elif choice == '3':
        print("You enter through the back entryway and decend a long staircase into the basement.")
        print("You hear whispers surrounding you in the shadows.")
        print("They get louder in louder until the pain of the sound is unbearable.")
        print("You curl up in pain. Unable to move you die a slow death.\n")
        print("GAME OVER.\n")
    elif choice == '4':
        print("You ascend the wall up to the terrace.")
        print("Entering through the terrace doorway you enter a master bedroom witha coffin in the center.")
        print("Suddenly, the head vampire emerges from the coffin.")
        finalPath()
    else:
        print("Invalid input!\n")
        entryPath()

# This function is a third path (1 of 2)
def frontPath():
    choice = input("1 - FLAME SPELL\n2 - INVISIBILITY POTION\n")
    if choice == '1':
        print("Fire swirls from your body, incinerating all the bats around you.")
        print("Your spell's emission is too powerful.")
        print("The wood surfaces catch fire and the mansion begins to burn quickly.")
        print("Suddenly, surrounded by flames, you find yourself face to face with the head vampire.")
        finalPath()
    elif choice == '2':
        print("You drink the potion but still cannot escape the bats!")
        print("They tear at your flesh until there is nothing left.\n")
        print("GAME OVER.\n")
    else:
        print("Invalid input!\n")
        frontPath()

# This function is a third path (2 of 2)
def gardensPath():
    choice = input("1 - STAB WITH WOODEN STAKE\n2 - SPARE THE CHILD\n")
    if choice == '1':
        print("You attempt to stab the vampire child with your wooden stake.")
        print("The child stops the stake with her bare hand, a force you've never felt in one so young.")
        print("Suddenly, the child morphs into something far more evil. The head vampire.")
        finalPath()
    elif choice == '2':
        print("You decide to spare the child.")
        print("How sad it is that someone so young has been forced into such a cruel fate.")
        print("And alas, such a young vampire would not be able to harm you.")
        print("But you were oh so wrong... The child pounces on you with a grip stronger than you've ever felt")
        print("\"Pathetic.\" Your body is torn to shreds.\n")
        print("GAME OVER.\n")
    else:
        print("Invalid input!\n")
        gardensPath()

# This function is the final path
def finalPath():
    print("\n\"You are powerful. I will make you an offer...")
    print("...Allow me to bite your neck and join me in taking over the kingdom...")
    print("...Or DIE!\"\n")
    choice = input("1 - BECOME A VAMPIRE\n2 - STAB HIM WITH WOODEN STAKE\n")
    if choice  == '1':
        print("The head vampire bites your neck.")
        print("Instead of taking your blood, his own blood flows from his teeth into your veins.")
        print("Your body pulses with energy.")
        print("Together, you lead a vampire army to take over the kingdom.")
        print("You kill every living thing that crosses your path.\n")
        print("GAME OVER. YOU WIN!\n")
    elif choice == '2':
        print("The head vampire teleports behind you just before the sharp point enters his heart.")
        print("\"Wrong choice.\"")
        print("That last thing you feel is a sharp pain on the back of your neck.")
        print("Your blood is completely drained from your body.\n")
        print("GAME OVER.\n")
    else:
        print("Invalid input!\n")
        finalPath()

# This block of code starts the program, gets the user's name, and calls the first path
print("\nVAMPIRE ADVENTURE!\n")
print("--- Written and programmed by Luke Demas ---\n")
name = input("What is your name, adventurer?\n")
print("You are " + name + ", the most famous vampire slayer in the land.")
print("You recieve a bounty to look into vampire sightings at the mysterious Ravenscreech Manor.")
print("Will you accept?\n")
introPath()