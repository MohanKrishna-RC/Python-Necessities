# # def get_speed(final, init, time_taken):
# #     speed = (final - init) / time_taken # simple equation could return negative value if init > final.
# #     assert speed >= 0 # will raise an AssertionError exception if speed is less than 0. 
# #     return speed

# # print(get_speed(5, 2, 1)) # will return 3 as expected 
# # print(get_speed(2, 5, 1)) # will raise AssertionError exception

# # Why Assertions ? 

# """
# The if else loop code would occupy more space, not only because it will
# branched inside an if statement but also because it will have to also raise an
# exception on a seperate line. Secondly it distracts us as a programmer from doing main job, which 
# isn't to defend all possible errors via a brute force method but
# to focus on the main code. Raising an exception allows for better error-handling and cleaner code.

# Better to use "try except"
# """

# """
# It is easy to fall into the trap of True Assertions: assertions whose conditions would never evaluate to False.
# For example, a tuple statement will always evaluate to True when non-empty. 
# """

# dict1={'k1':1, 'k2':'two'}
# print('{}\n{}'.format('Line 1','\n'.join('{}:{}'.format(k,v) for k,v in dict1.items())))


# """ f-string format :
# f-string, also called formatted string literal, is pretty much identifical to
# """
# var1='abc'
# print(f'{var1.upper()}')



