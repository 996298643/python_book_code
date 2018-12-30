import array

a = array.array("B", [1, 2, 3])

a.append(4)

print(a)

a = a + a

print(a)

a = a[2 : -1]

print(a)

print(a.tostring())

for s in a :
    print(s)