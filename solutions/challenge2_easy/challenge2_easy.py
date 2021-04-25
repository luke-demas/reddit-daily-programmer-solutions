# r/dailyprogrammer
# challenge 2, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

# solution by Luke Demas

# This function solves for force, F = M * A
def forceCalc():
    mass = input("What is mass (M)?\n")
    acceleration = input("What is acceleration (A)?\n")
    force = float(mass) * float(acceleration)
    print("Force (F) = " + str(force))

# This function solves for mass, M = F / A
def massCalc():
    force = input("What is force (F)?\n")
    acceleration = input("What is acceleration (A)?\n")
    mass = float(force) / float(acceleration)
    print("Mass (M) = " + str(mass))

# This function solves for acceleration, A = F / M
def accelerationCalc():
    force = input("What is force (F)?\n")
    mass = input("What is mass (M)?\n")
    acceleration = float(force) / float(mass)
    print("Acceleration (A) = " + str(acceleration))

# The following handles initial user input and routes to specified function
print("Welcome to Newton's Second Law of Motion Calculator!\nWhat would you like to solve for?\n")
choice = input("(F, M, A)\n")

if choice == 'F':
    forceCalc()
elif choice == 'M':
    massCalc()
elif choice == 'A':
    accelerationCalc()