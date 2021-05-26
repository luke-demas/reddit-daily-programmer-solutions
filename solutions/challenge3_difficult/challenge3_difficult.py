# r/dailyprogrammer
# challenge 3, difficult
# https://www.reddit.com/r/dailyprogrammer/comments/pkwgf/2112012_challenge_3_difficult/

# solution by Luke Demas

scrambled_words = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle', 'nalraoci', 'nsdeuto', 'amrhat', 'inknsy', 'iferkna']

file = open('wordlist.txt', 'r')
word_list = []
for line in file:
    word_list.append(line.strip())
word_list.sort(key=len)
file.close()

for word in word_list:
    for scrambled in scrambled_words:
        if ''.join(sorted(scrambled)) == ''.join(sorted(word)):
            print(scrambled + " -> " + word + "\n")