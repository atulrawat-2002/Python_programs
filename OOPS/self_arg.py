class Chai:

    def __init__(self, type_, size):
        self.type_ = type_
        self.size = size
    
    def summary(self):
        return f"{self.size} ml of {self.type_}"
    
ginger = Chai("Ginger", 200)

black = Chai("Black", 190)

print(black.summary())
print(ginger.summary())