# r/dailyprogrammer
# challenge 1, difficult
# https://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/

# solution by Luke Demas

max_num = 100
min_num = 1
guess_num = 0
response = "null"

print("Think of a number from 1 - 100. I'll guess your number :)")

while response != "y":
    guess = int((max_num + min_num)/2)
    guess_num += 1
    response = input("Is your number " + str(guess) + "? (y) -- yes, (h) -- higher, (l) -- lower\n")   
    if response == "y":
        print("Number guessed in " + str(guess_num) + " guesses!")
    elif response == "h":
        min_num = guess
    elif response == "l":
        max_num = guess
    else:
        print("Invalid input.")
        guess_num -= 1
    