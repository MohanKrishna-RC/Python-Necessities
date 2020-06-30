import sys

#Read the content from the file in a path in the format of '.txt' or '.pdf' etc
def FileTextcount(fileInput):

    linescount = 0
    wordscount = 0
    charscount = 0

    with open(fileInput,'r') as file :
        content = file.read()
        print("\nContent of the file :\n", content)

    with open(fileInput,'r') as file:
        for lines in file:
            words = lines.split()
            linescount +=1
            wordscount = len(words)

            charscount += len(lines) - lines.count('  ')
        
    print("\nNumber of Lines : %s" % str(linescount))
    print("\nNumber of words : %s" % str(wordscount))
    print("\nNumber of Chars : %s" % str(charscount))


if __name__ == "__main__":
    linesInput = input("\nEnter path of the text file : ")
    FileTextcount(linesInput)


