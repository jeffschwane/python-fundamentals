'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

words = []
with open("/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/08_file_io/words.txt", "r") as f_in:
    for line in f_in.readlines():
        words.append(line)
for word in words:
    word = word.rstrip()
    word = word[::-1]
with open("/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/08_file_io/words_reverse.txt", "w") as f_out:
    f_out.write("\n".join(words))
