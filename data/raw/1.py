def mymethod(self):
    return self.x > 100
class_name = "MyClass"
base_classes = tuple()
params= {"x": 10, "check_greater": mymethod}
MyClass = type("MyClass", base_classes, params)
obj = MyClass()
print(obj.check_greater())