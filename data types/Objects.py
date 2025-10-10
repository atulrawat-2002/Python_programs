# sugar = 2
# print(f"initial sugar amount is : {sugar} and id is: {id(sugar)}")
# sugar = 12
# print(f"After sugar amount is : {sugar} and id is: {id(sugar)} " )

spice_set = set()
print(spice_set, {id(spice_set)})
spice_set.add("Ginger")
spice_set.add("Cardamom")
print(spice_set, {id(spice_set)})