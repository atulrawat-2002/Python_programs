class BaseChai:

    def __init__(self, type_):
        self.type_ = type_

    def prepare(self):
        print(f"The {self.type_} chai is getting prepared")

class MasalaChai(BaseChai):

    def add_spice(self):
        print(f"Adding cardamom, clove, ginger")

class ChaiShop:
    chaicls = BaseChai

    def __init__(self):
        self.chai = self.chaicls("regular")

    def serve(self):
        print(f"Serving {self.chai.type_} chai")
        self.chai.prepare()

class FancyChai(ChaiShop):
    chaicls = MasalaChai


shop = ChaiShop()
fancy = FancyChai()

shop.serve()
fancy.chai.add_spice()