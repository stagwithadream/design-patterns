# only one instance of this class exists ever

# this __new__ method is inherited from object class. and is always called when a new
# object is created, we are controlling this by overwriting this.

# super method is used to reference the upper class, in this case it is object class of python,
# this __new__ method in object class is responsible for returning the instance of the class cls

class singleton:
    #  this variable is used to store the single instance of this class
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls) # call base classe's __new__ method
        return cls._instance

if __name__ == "__main__":
    s1 = singleton()
    s2 = singleton()
    print(id(s1))
    print(id(s2))
    print(s1 is s2)


# instantiate the object of a class - __new__
# initialize the object of a class __init__, this is called after the obj is instantitated

# cls _> ref to the class.  'this' for a class
# self -> ref to an object. 'this' for an object=