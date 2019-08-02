from library import Base

# assert hasattr(Base,"foo"),"naam gad bad hai"

class Derived(Base):
    def bar(self):
        return "bar"

