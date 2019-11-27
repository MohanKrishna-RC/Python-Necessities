import pandas as pd

''' Unliked sequenced data types like lists and tuples, where indexing is achieved using positional indices, dictionaries are indexed using their keys.
Therefore, individual values can be accesed using these keys '''

empty_dict = {}

job1 = { "title" : "Production Manager",
"location" : "Rest of thailand",
"job_type" : "Full Time",
"employer" : "The Bakchodi talent Comapny",
"category" : "Faming"
}

''' We just created a dictionary with some of the keys and assigned it to the variable job1 '''

''' Dictionaries can also be created using the dict() constructor. To do
this we pass the constructor a sequence of key-value pairs. We could also pass in named arguments. '''

# create an empty dictionary
empty_property = dict()

# create dictionary using a list of key-value tuples
job2 = dict([
  ("title","Marketing & Business Development Manager"),("location","Mombasa"),
  ("job_type","Full Time"),
  ("employer","KUSCCO Limited (Kenya Union of Savings & Credit Co-operatives Limited)"),
  ("category","Marketing & Communications")
])

# Using keyword arguments
dict(
  title="Marketing & Business Development Manager",
  location="Mombasa",job_type="Full Time",
  employer="KUSCCO Limited (Kenya Union of Savings & Credit Co-operatives Limited)",
  category="Marketing & Communications"
)

''' Dictionaries are indexed using their keys. To access a particular value in a dictionary we use the indexing operator ( key inside the square bracket).
However, to use this method, we need to make sure the key we intend to retrieve exists, lest we get a "KeyError".
Checking for avaialability of a key is as easy as using the "in" operator. '''

# Check existence of title
"title" in job2 # returns True

"salary" in job2 # returns False

# Using key indexing
job2["title"] # return 'Marketing & Business Development Manager'

''' We have a better tool - the get() method.  This method works by giving out a value if the key exists, or returning "None".'''

#Modification

''' Dictionaries can be modified directly using the keys or using the update() method. 
update() takes in a dictionary with the key-value pairs to be modified or added. '''

# Adding a new entry for salary using the index
job2["salary"] = 10000

# Modifying the entry for job_type using the index
job2["job_type"] = "Part time"

# Modifying the salary entry using update
job2.update({"salary":20000})

# Adding the available entry using update
job2.update({"available":True})

''' A particularly nice use case for update() is when we need to merge two dictionaries.
Say we have another dictionary extra_info containing extra fields for a job, and we would like to merge this with job2 '''


extra_info = {
  "verified":True,
  "qualification":"Undergraduate Degree",
  "taxable":True}

# Merge extra_info with job2
job2.update(extra_info)

#deletion

del job2["salary"]
del job2["available"]
print(job2) #return a dictionary without 'salary' and 'available' entries

job1.clear()
print(job1) #return an empty dictionary

del job1
print(job1) # return NameError


# iteration

''' A dictionary by itself is an iterable of its keys. Moreover, we can iterate through dictionaries.

dict.values() - this returns an iterable of the dictionary's values.
dict.keys() - this returns an iterable of the dictionary's dict_keys
dict.items() - this returns an iterable of the dictionary's ( key, value pairs) '''


# Speeding up our code

''' Dictionary unpacking can greatly speed up our code. It invloves destructing a dictionary into individual keyword arguments with
values. 

This is especially useful for cases that involve supplying multiple keyword arguments, 
for example in function calls.

To implement this functionality we use the iterable unpacking operator (**)''' 

import csv
#Define a Job Class
class Job:
    def __init__(self,
                 title="Job Title",
                 location="Job Location",
                 job_type="Job Type",
                 employer="Job Employer",
                 category="Job Category",):       
        self.title = title
        self.location = location
        self.job_type = job_type
        self.employer = employer
        self.category = category
    def __str__(self):
        return self.title

# Creating a job object without unpacking
Job("Marketing & Business Development Manager","Mombasa","Full Time",
    "KUSCCO Limited (Kenya Union of Savings & Credit Co-operatives Limited)",
    "Marketing & Communications")

with open('jobs.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    for job in reader:
        
        # Creating a job object with unpacking
        Job(**job)
