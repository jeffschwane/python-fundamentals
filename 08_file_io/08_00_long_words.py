'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
words = []
with open("/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/08_file_io/words.txt", "r") as f_in:
    for line in f_in.readlines():
        words.append(line)
for word in words:
    if len(word) > 20:
        print(word)
