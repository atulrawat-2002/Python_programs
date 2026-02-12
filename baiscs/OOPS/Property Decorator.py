class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age == 5:
            raise ValueError("Tea leaf must be between 1 and 5 years")
        else:
            raise ValueError("Tea leaf must be between 1 and 5 years")
         
    
leaf = TeaLeaf(19)

print(leaf.age)