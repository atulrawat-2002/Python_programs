chai_type = "ginger chai"
customer_name = "Priya Ram Kapoor"

# print(f"Order for {customer_name} and order is {chai_type}")

chai_description = "Aromatic and Bold More"

# print(f"first word is {chai_description[:8]}")
# print(f"last word is {chai_description[13:]}")
# print(f"last word is {chai_description[::-1]}")

label = "á é í ó ú Á É Í Ó Ú ñ Ñ"
encoded_label = label.encode("utf-8")
print(f"{encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"decoded string is {decoded_label}")