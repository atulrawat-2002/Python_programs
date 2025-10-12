seat_type = input("Enter your prefered seat type(sleeper/general/AC): ").lower()

match seat_type:
    case "sleeper":
        print('Your seat is booked as sleeper')
    case "ac":
        print("your seat is booked as AC")
    case "general":
        print("Your seat is booked as general")
    case _:
        print("Please choose a valid option!")
    