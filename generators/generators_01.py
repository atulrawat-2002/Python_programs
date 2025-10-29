def get_chai_list():
    yield "This is cup 1"
    yield "This is cup 2"
    yield "This is cup 3"

stall = get_chai_list()

# for i in stall:
#     print(i)


def chai_fun():
    return ["cup 1", "cup 2", "cup 3"]

def chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

gen_chai = chai_gen()

print(next(gen_chai))
print(next(gen_chai))
print(next(gen_chai))
print(next(gen_chai))

# for i in gen_chai:
#     print(i)

# print(chai_fun())