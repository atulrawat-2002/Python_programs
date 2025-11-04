class ChaiOrder:

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size


    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            dict_data["tea_type"],
            dict_data["sweetness"],
            dict_data["size"]
        )
        
    
    @classmethod
    def from_string(cls, string_data):
        tea_type, sweetness, size = string_data.split("-")
        return cls(tea_type, sweetness, size)

# obj1 = ChaiOrder.from_dict({
#     "tea_type": "Black Tea",
#     "sweetness": "One Spoons",
#     "size": "Small"
# })

obj1 = ChaiOrder.from_string("Green-Two Spoons-Large")

print(obj1.__dict__)

# obj = ChaiOrder("Ginger", "Two spoons", "Medium")
# print(obj.tea_type, obj.size, obj.sweetness)