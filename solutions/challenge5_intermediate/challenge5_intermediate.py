# r/dailyprogrammer
# challenge 5, intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/pnhtj/2132012_challenge_5_intermediate/

# solution by Luke Demas

anagrams = 0
word_list = []

text = open('anagram.txt', 'r')
for line in text:
    for word in line.split():
        word_list.append(word)
text.close()

for word1 in word_list:
    for word2 in word_list:
        if word1 == word2:
            pass
        else:
            if sorted(word1) == sorted(word2):
                print(word1 + " <-> " + word2)
                word_list.remove(word1)
                word_list.remove(word2)
                anagrams += 1

print("\nNumber of anagrams: " + str(anagrams))
    