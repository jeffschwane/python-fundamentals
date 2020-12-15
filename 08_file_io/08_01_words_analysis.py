'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

words = []
with open("/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/08_file_io/words.txt", "r") as f_in:
    for line in f_in.readlines():
        words.append(line)
word_length = {}
min_words = []
max_words = []
for word in words:
    word = word.rstrip()
    word_length[word] = len(word)
max_word = (max(word_length, key=word_length.get))
min_word = (min(word_length, key=word_length.get))
for k, v in word_length.items():
    if v == word_length[max_word]:
        max_words.append(k)
    if v == word_length[min_word]:
        min_words.append(k)

print(f'The shortest word are: {min_words}')
print(f'The longest words are: {max_words}')
print(f'The total number of words in the file is {len(words)}')
