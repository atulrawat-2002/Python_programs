chai_order = {"masals": 30, "Ginger": 40}

try:
    print(chai_order["Cardamom"])
except KeyError:
    print("The key you are referring does not exit")

print("hello")