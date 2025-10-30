def local_chai():
    yield "ginger chai"
    yield "masala chai"

def imported_chai():
    yield "Oolong chai"
    yield "Matcha chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

get_chai = full_menu()

for chai in get_chai:
    print(chai)