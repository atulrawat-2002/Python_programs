class chai:
    temperature = "Hot"
    strength = "Strong"

cutting = chai()

print(f"temperature of the object {cutting.temperature}")

cutting.temperature = "Cold"
cutting.cup = "medium"

print(f"temperature of the class {chai.temperature}")

del cutting.cup

del cutting.temperature

print(cutting.cup)
print(f"temperature of the object {cutting.temperature}")