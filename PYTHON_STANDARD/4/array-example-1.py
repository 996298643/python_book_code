import array

a = array.array("B",  range(16))  #unsigned charr

b = array.array("h",  range(16)) #signed

print(a)

print(repr(a.tostring()))

print(b)

print(repr(b.tostring()))