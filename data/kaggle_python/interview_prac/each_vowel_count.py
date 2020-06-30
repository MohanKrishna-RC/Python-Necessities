import numpy as np
import sys
vowels = 'aeiou'

ip_str = input("Enter the string :" )

#make the string suitable for caseless comparisons

ip_str = ip_str.casefold()

print(ip_str)

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels

for char in ip_str:
    if char in count:
        count[char]+=1
print(count)
