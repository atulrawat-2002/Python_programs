menu = [
    "Ginger Tea",
    "Black Tea",
    "Iced Tea",
    "Iced Coffee"
    ]

iced_item = [item * 2 for item in menu if len(item) >= 10]

print(iced_item)