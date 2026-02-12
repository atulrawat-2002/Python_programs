import csv
import os

FILENAME = "contacts.txt"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["name"] == name:
                return
        
        with open(FILENAME, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, phone, email])
            print("Contact added! ")

def view_contact():

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        rows = list(reader)

        if len(rows) < 1:
            print("No contact found! ")

        print("\n Your contacts: \n")

        for row in rows[:2]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to be serched: ")
    found = False

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        for row in reader:
            if term in row["Name"].lower():
                print(f" {row["Name"]} | {row["Phone"]} | {row["Email"]} ")
                found = True
    if found:
        print("contact not found! ")


def main():

    while True:
        print("\n Contact Book ")
        print("1. Add contact ")
        print("2. View All Contact ")
        print("3. Search Contact ")
        print("4. Exit ")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            break
        else:
            print("Choose a valid choice")

main()