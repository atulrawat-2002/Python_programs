# def add(a, *args, **kwargs):
#     print(a, args)
#     for key, value in kwargs.items():
#         print(key, value)

# add(3, 4, 5 ,name="Atul", age=23, gender="male")



add = lambda a, b: a + b
print(add(2, 3))

# # r = range(5)
# # # print(r)
# # # print(list(r))

# # if 5 in range(19):
# #     print(True)


# # arr = [3, 4, 5, 6,7 ]
# str = "Atul"

# for i in enumerate(str):
#     index, value = i
#     print(index, value)

# def greet():
#     print("hello")
#     return 0

# x = greet()
# print(x)

# def add(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add(4, 5, 6, 7))