#class definition
class House:
    pass

# Create an object of House class using its constructor
first_house = House()
# check type of the object we just created
print(type(first_house))

''' # Output
<class '__main__.House'> '''

# Create a class for constructing a house.
class House:
    #defining a instance method
    def set_rooms(self,num_rooms):
        self.rooms = num_rooms


#Object is a particular instance of a class.
#Instance Methods are the "functions" defined in a class and are called using the objects of the class.

#creating a instance of the class
house_small = House()

#Now we're calling the instance method for the created instance
house_small.set_rooms(2)

#creating another instance
house_big = House()
house_big.set_rooms(5)

print("No of rooms in small house: {}".format(house_small.rooms))
print("No of rooms in big house: {}".format(house_big.rooms))

#Defining the Initializer Method.

class House:
    #  Initializer
    def __init__(self,num_rooms):
        self.rooms = num_rooms

    #Create instances of the class

house_small = House(2)
house_big = House(5)

print("No of rooms in small house: {}".format(house_small.rooms))
print("No of rooms in big house: {}".format(house_big.rooms))


#Inheritance

#Base class
class BaseClass:
    pass

# Derived class
class DerivedClass(BaseClass):
    pass

#Intution for Inheritance.

class Apartment:
    ''' 
    A house within a large building along with other houses 
    '''
    def __init__(self,rooms,bathrooms,floor):
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.floor = floor

    def room_details(self):
        print("This property has {} rooms with {} bathrooms".format(self.rooms,self.bathrooms))

appa = Apartment(3,2,5)
appa.room_details()

class Bungalow:
    ''' 
    A typically one-story landed house
    '''

    def __init__(self,rooms,bathrooms):
        self.rooms = rooms
        self.bathrooms = bathrooms

    def room_details(self):
        print("This property has {} rooms with {} bathrooms".format(self.rooms,self.bathrooms))


''' If we observe keenly we found that both the classes have some common properties and also
common behavior. Currently, these common properties and behavior are being duplicated in both the classes, which can easily be extracted out in order to be re-used.
This is where the concept of Inheritence can be of help.'''

''' Let's try to create a Base class with all the common properties, and result the same in the base class. '''

class House:
    ''' A place which provides with shelter or accomodation '''
    def __init__(self,rooms,bathrooms):
        self.rooms = rooms
        self.bathrooms = bathrooms

    def room_details(self):
        print("This property has {} rooms with {} bathrooms".format(self.rooms,self.bathrooms))

class Apartment(House):
    ''' 
    A house with a large building where others also have their own house
    '''

    def __init__(self,rooms,bathrooms,floor):
        House.__init__(self,rooms,bathrooms)
        self.floor = floor

class Bungalow(House):
    ''' A typically one-story landed House '''
    pass

apartment = Apartment(2,2,14)
apartment.room_details()

bungalow = Bungalow(4,3)
bungalow.room_details()






####################################################################################

class Housing:
    def __repr__(self):
        return "This complete code is for describing the housing system"

housing = Housing()

print(housing)