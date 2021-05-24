# r/dailyprogrammer
# challenge 3, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

# solution by Luke Demas

# ord('A') == 65
# ord('a') == 97
option = input("(e)nocde or (d)ecode?\n")
if option == "e":
    text = input("Enter text to encode:\n")
    shift = int(input("Enter shift number:\n"))
    new_text = ''
    for character in text:
        if character.isupper():
            new_text += chr(((ord(character) - 65) + shift) % 26 + 65)
        elif character.islower():
            new_text += chr(((ord(character) - 97) + shift) % 26 + 97)
    print(new_text)
elif option == "d":
    text = input("Enter text to decode:\n")
    shift = int(input("Enter shift number:\n"))
    new_text = ''
    for character in text:
        if character.isupper():
            new_text += chr(((ord(character) - 65) - shift) % 26 + 65)
        elif character.islower():
            new_text += chr(((ord(character) - 97) - shift) % 26 + 97)
    print(new_text)
