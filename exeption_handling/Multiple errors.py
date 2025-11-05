def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price // quantity
        print(f"{price} and Total cost is {cost}")
    except KeyError:
        print("sorry we do not have that item!")
    except TypeError:
        print("Please enter a valid value")

item = input("enter the item: ")

quantity = int(input("enter the quantity: "))
process_order(item, quantity)