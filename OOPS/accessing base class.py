class Chai:
    def __init__(self, type_, strength):
        self.type_ = type_
        self.strength = strength


# class GingerChai(Chai):
#     def __init__(self, type_, strength, sugar):
#         Chai.__init__(self, type_, strength)
#         self.sugar = sugar

#     def summary(self):
#         print(f"The {self.type_} is {self.strength} and having {self.sugar} sugar")

class GingerChai(Chai):
    def __init__(self, type_, strength, sugar):
        super().__init__(type_, strength)
        self.sugar = sugar

    def summary(self):
        print(f"The {self.type_} is {self.strength} and having {self.sugar} sugar")


obj = GingerChai("Ginger", "light", "High")

obj.summary()