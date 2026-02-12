essential_spices = {"ginger", "cardamom", "black pepper"}

optional_spices = {"cloves", "ginger"}

all_spices = essential_spices | optional_spices

common_Spices = essential_spices & optional_spices

print(f"all spices are {all_spices}")

# print(f"common spices are {common_Spices}")

only_in_essential = essential_spices - optional_spices

# print(f"only in essential spices are {only_in_essential}")

# membership test

print(f"is clove in essential spices {'cloves' in all_spices}")