class BaseMeta(type):
    def __new__(cls,name,bases,body):
        if not 'bar' in body:
            raise TypeError("Bad user class")
        # print('BaseMeta.__new__',cls,name,bases,body)   
        return super().__new__(cls,name,bases,body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    def __init_subclass__(cls,*a,**kw):
        print('init_subclass',a,kw)
        return super().__init_subclass__(*a,**kw)
# old_bc = __build_class__ 

# def my_bc(*a,**kw):
#     print("my buildclass-->",a,kw)
#     return old_bc(*a,**kw)

# import builtins
# builtins.__build_class__ = my_bc

