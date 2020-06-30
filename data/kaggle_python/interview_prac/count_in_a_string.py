"""
Count number of lines, number of words and number of characters (excluding space)
"""

import sys

def textCount(line):
    linescount = 0
    wordscount = 0
    charscount = 0

    # splitting the string and stroing the list in words variable

    words = line.split()
    print(words)
    linescount += 1 #incrementing lines count
    wordscount += len(words)

    #counting number of character excluding spaces

    charscount += len(line) - line.count('  ')

    print("\nNumber of Lines : %s" % str(linescount))
    print("\nNumber of words : %s" % str(wordscount))
    print("\nNumber of Chars : %s" % str(charscount))


if __name__ == "__main__":
    linesInput = input("\nEnter a Line : ")
    textCount(linesInput)