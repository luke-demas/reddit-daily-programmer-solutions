# r/dailyprogrammer
# challenge 4, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/

# solution by Luke Demas

# Random Password Generator

import random

print("Random Password Generator by Luke Demas\n")
num = input("Number of passwords to generate?\n")
length = input("Length of passwords generated?\n")

for i in range(int(num)):
    print(''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*' * int(length), int(length))))