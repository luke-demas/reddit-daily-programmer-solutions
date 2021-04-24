# r/dailyprogrammer
# challenge 1, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/

# solution by Luke Demas

name = input("What is your name?\n")
age = input("What is your age?\n")
user = input("What is your reddit username?\n")
info = "your name is " + name + ", you are " + age + " years old, and your username is " + user + "\n"
print(info)
with open('log.txt', 'a') as log:
    log.write(info)
