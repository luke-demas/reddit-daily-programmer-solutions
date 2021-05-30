# r/dailyprogrammer
# challenge 5, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/

# solution by Luke Demas

logged_in = False

login_file = open('login.txt', 'r')
login_data = login_file.read().split('\n')
login_file.close()

username = input('Username: ')
password = input('Password: ')

if username == login_data[0] and password == login_data[1]:
    logged_in = True

if logged_in:
    print("Log in succesful.\n\nThis message is secret! Only logged in users can see it!")
else:
    print("Username or password is incorrect.")