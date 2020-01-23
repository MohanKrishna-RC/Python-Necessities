"""
Stack : 

Unlike any array structure, which allows randome access at all positions, a stack limits
the inserting and removing operation to only one side of the data
sequence. A stack follows the last in, First out (LIFO) principle.

In python, stack can be implemented using a list. To follow the LIFO principle,
inserting and removing operations both occur at the tail of the list.

"""
class stack:
  # by default pass in [] as inivial value
  def __init__(self,initialVal=[]):
    self.stack = initialVal
  
  # push is to append to the tail of the list
  def push(self,ele):
    self.stack.append(ele)
    return self.stack
  
  # pop is to remove from the tail of the list
  def pop(self):
    return self.stack.pop(-1)
  
  def checkStack(self):
    print([ele for ele in self.stack])
  
  def checkTop(self):
    print(self.stack[-1])


"""
Queue:

Similar to slack, the queue also limits the position for inserting and removing an operation on a sequence of data. However, unlike a stack, a queue follows
the first in, first out (FIFO) principle.

In python, a queue can also be implemented using a list. To follow the FIFO principle, the inserting
operation occurs at the tail of the list, while the removing operation occurs at the head of the list.
"""
class queue:
  # by default pass in [] as inivial value
  def __init__(self,initialVal=[]):
    self.queue = initialVal
  
  # enqueue is to append to the tail of the list
  def enqueue(self,ele):
    self.queue.append(ele)
    return self.queue
  
  # dequeue is to remove from the head of the list
  def dequeue(self):
    return self.queue.pop(0)
  
  def checkQueue(self):
    print([ele for ele in self.queue])
  
  def checkHead(self):
    print(self.queue[0])
  
  def checkTail(self):
    print(self.queue[-1])

"""
Set : 
A set object is an unordered collection of distinct hashable objects. It's one of Python's built in types and allows the 
dynamic adding and removing of elements, iteration, and operations with another set objects.

"""
""" SET """

# # set initialization by passing in a list
# myset = set([1,2,3,3,3])

# # set initialization using {}
# myset = {1,2,3,3,3}

# # iteration of set
# for ele in myset:
#   print(ele)

# # check if ele in set:
# print(True if ele in myset else False)

# # add an element to set:
# myset.add(ele)

# print(myset)

# # # remove an element from set
# myset.remove(ele)
# print(myset)

# # # get length of the set
# print(len(myset))


# myset1 = {1,2,3}
# myset2 = {1,2,4,5}

# # union
# myset = myset1.union(myset2)
# print(myset)

# # intersection
# myset = myset1.intersection(myset2)
# print(myset)

# # difference
# myset = myset1.difference(myset2)
# print(myset)

"""
Dicitonary:

A dictionary contains mapping information of (key,value) pairs. Given a key, the corresponding
value can be found in the dictionary. It's also one of Python's built in types. The (key,value) pairs can be dynamically added, removed, and modified.
A dicitonary also iteration through the keys, values, and (key,value) pairs
"""
# dictionary initialization using {}
mydict = {'a':1,'b':2}
print(mydict)

# add new (key,value) pair
mydict['c'] = 3
print(mydict)

# modify existing (key,value) pair
mydict['a'] = 5
print(mydict)

# remove (key,value) pair
mydict.pop('a')
print(mydict)

# get length of the dictionary
print(len(mydict))

# iteration through keys
for key in mydict.keys():
    print(key)

# iteration through values
for value in mydict.values():
    print(value)

# iteration through (key,value) pairs
for key,value in mydict.items():
    print(key,value)


"""
Linked List :

A linked list is a linear data structure, with the previous node pointing to the next node. 
It can be implemented by defining a ListNode class.
"""
"""  Linked List """

class ListNode:
  def _init_(self,val):
    self.val = val
    self.next = None

# initiation of linked list
headNode = ListNode(1)
secondNode = ListNode(2)
thirdNode = ListNode(3)

headNode.next = secondNode
secondNode.next = thirdNode

# iterate through the linked list
curNode = headNode
while curNode:
  print(curNode.val)
  curNode = curNode.next

# insert new listnode with value of 5 in between the secondNode and thirdNode
curNode = headNode
while curNode.val != 2:
  curNode = curNode.next
newNode = ListNode(5)
newNode.next = curNode.next
curNode.next = newNode

# remove the listnode with value of 5
curNode = headNode
while curNode.next.val != 5:
  curNode = curNode.next
  curNode.next = curNode.next.next



        












