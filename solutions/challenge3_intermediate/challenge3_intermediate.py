# r/dailyprogrammer
# challenge 3, intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/pkwb1/2112012_challenge_3_intermediate/

# solution by Luke Demas

# PLAINTEXT ALPHABET:  abcdefghijklmnopqrstuvwxyz
# CIPHERTEXT ALPHABET: zyxwvutsrqponmlkjihgfedcba

# EXAMPLE DECODE (whith whitespace, numbers, and symbols ignored):
# gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt
# the quick brown fox jumps over the lazy dog

option = input("(e)nocde or (d)ecode?\n")
if option == 'e':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    symbols = ' !@#$%^&*()-_=+[]{}/\|;:\'",.<>?'
    alpha_trans = str.maketrans(alphabet, alphabet[::-1], '')
    num_trans = str.maketrans(numbers, numbers[::-1], '')
    symb_trans = str.maketrans(symbols, symbols[::-1], '')
    text = input("Enter text to encode:\n")
    choice = input("Encrypt whitespace, numbers, and symbols? (y or n)\n")
    new_text = text.lower().translate(alpha_trans)
    if choice == 'y':
        new_text = new_text.translate(num_trans)
        new_text = new_text.translate(symb_trans)
    print(new_text)
elif option == 'd':
    alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    numbers = '9876543210'
    symbols = '?><.,"\':;|\/}{][+=_-)(*&^%$#@! '
    alpha_trans = str.maketrans(alphabet, alphabet[::-1], '')
    num_trans = str.maketrans(numbers, numbers[::-1], '')
    symb_trans = str.maketrans(symbols, symbols[::-1], '')
    text = input("Enter text to decode:\n")
    choice = input("Decrypt whitespace, numbers, and symbols? (y or n)\n")
    new_text = text.lower().translate(alpha_trans)
    if choice == 'y':
        new_text = new_text.translate(num_trans)
        new_text = new_text.translate(symb_trans)
    print(new_text)
