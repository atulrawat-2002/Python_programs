class A:
    label = "A: base call"

class B(A):
    label = "B: class B"

class C(A):
    label = "C: class C"

class D(C, B):
    pass

obj = D()
print(D.__mro__)

print(obj.label)