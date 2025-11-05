def serve_chai(flavor):
    try:
        if flavor not in ["masala", "ginger"]:
            raise ValueError(f"The {flavor} chai is not available")
        else:
            print(f"The {flavor} chai is getting ready...")

    except ValueError as e:
        print("Sorry!", e)
    finally:
        print("Next customer please!")
    


flavor = input("Enter the flavor: ")

serve_chai(flavor)