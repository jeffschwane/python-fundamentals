""" Searches a folder you specify (as well as all its subfolders) on your computer and compiles a list of all .jpg files. The list should contain the complete path of each .jpg file
"""

import os
dir = input('Specify a folder directory to search for .jpg files: ')
for file in os.listdir(dir):
    if file.endswith(".jpg"):
        print(os.path.join(dir, file))
