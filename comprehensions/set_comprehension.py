menu = [
    "Chai",
    "Water",
    "Pani Puri",
    "Chai",
    "Water",
    "Pani Puri",
    "Ghee"
]

# print(menu)

uniques = {item for item in menu if len(item) >= 4}

print(uniques)

