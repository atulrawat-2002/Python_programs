studen_data = dict(name="Atul", course="Post Graduation", roll_no=21)

# print(f"This is the data of student {studen_data}")

class_dettail = {}

class_dettail["name"] = "Computer Graphics"

class_dettail["time"] = "4 a.m."


class_dettail["time"] = "5 p.m."

# print(f"This is the class data {class_dettail}")

del class_dettail["name"]
# print(f"This is the class data {class_dettail}")

studen_data = {"name":"Atul", "roll":23, "friends":6, "course": "python"}

# print(f"all the keys are {studen_data.keys()}")

# print(f"all the values are {studen_data.values()}")

# print(studen_data)

chai_recipe = dict(type="normal", color="black")

item = chai_recipe.get("ingredients", "Not specified")

print(item)