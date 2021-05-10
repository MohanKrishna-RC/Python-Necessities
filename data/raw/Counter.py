#A counter tool is provided to support convenient and rapid tallies.
from collections import Counter
# Tally occurrences of words in a list 
cnt = Counter()
for word in['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] +=1
print(cnt)  #Counter({'blue': 3, 'red': 2, 'green': 1})

# Find the ten most common words in Hamlet 
import re 
words =re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
# [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631)
# ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

"""
A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as 
dictionary keys and their counts are stored as dictionary values.
Counts are allowed to be any integer value including zero or negative counts.
The counter class is similar to bags or multisets in other languages.

Hashable : An object is said to be hashable if it has a hash value that remains the same during its lifetime. 
If hashable objects are equal when compared, then they have same hash value. 
Being hashable renders an object usable as a dictionary key and a set member as these data structures use hash values internally.

Hash values are just integers that are used to compare dictionary keys during a dictionary lookup quickly.

Internally, hash() method calls __hash__() method of an object which is set by default for any object.
"""

# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:',hash(181.23))

# hash for string
print('Hash for Python is:', hash('Python'))
"""
Hash for 181 is: 181
Hash for 181.23 is: 530343892119126197
Hash for Python is: 2230730083538390373 
"""

c = Counter(a=4,b=2,c=0,d=-2)
list(c.elements())

"""
Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a KeyError:
"""

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c +=Counter()                  # remove zero and negative counts

"""
#OrderedDict 

OrderedDict dictionaries are just like regular dicitonaries but they remember the order that items
were inserted. When iterating over an ordered dictionary, the items are returned in the order their keys were first added.

OrderedDict.popitem(last=True)

The popitem() method for ordered dictionaries returns and removes a (key,value) pair.
The pairs are returned in LIFO order if last is true or FIFO order if false.

In addition to the usual mapping methods, ordered dictionaries also support reverse
iteration using reverse().
"""

d ={'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# dictionary sorted by key
OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# dictionary sorted by value
OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# dictionary sorted by length of the key string
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
"""
The  new  sorted  dictionaries  maintain  their  sort  order  when  entries  are  deleted.  
But when  new  keys  are  added,  the  keys  are  appended  to  the  end  and  the  sort  is  not maintained.
"""