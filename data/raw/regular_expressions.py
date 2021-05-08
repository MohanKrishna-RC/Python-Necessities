"""
\d - Matches any decimal digit, this is equivalent to the set class [0-9]
\D - Matches any non-digit character
\s - Matches any whitespace character
\S - Matches any non White space character
\w - Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9...]
\W - Matches any non-alphanumeric character
"""

import re
txt = "That will be 59 dollars"

"""
The Sub function replaces the matches with the text of our choice
"""

# Replace every white-space character with &
print(re.sub(r"\s","&",txt))

#dollars will replace with rupes
print(re.sub('dollars','rupees',txt))

"""
The split function returns a list where the string has been split at each match
"""
txt = "That will be 59 dollars"
# Split at each white-space character
x= re.split(r"\s",txt)
print(x)

#Split the string only at the first occurence
x= re.split(r"\s",txt,1)
print(x)

"""
Search() function searches the string for a match, and returns a Match object if there is a match.
"""
txt = "That will be 59 dollars"
#Search for first white space character in the string
x3 = re.search("\s",txt)
print("the first white-space",x3.start())

# Either or
x4 = re.search("That|that",txt)
print(x4)

#Print a list of all matches
x5 = re.search("wi",txt)
print(x5)

#Return an empty list if no match was found
x6 = re.search("sun",txt)
print(x6)

""" Examples """

import re

def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,text):
        return 'Found Match'
    
    else:
        return 'Match Not found'

print(text_match('cab_cjsgfj'))
print(text_match('cag_Ahsjsfhyd'))
print(text_match('Abdf_dfdfd'))