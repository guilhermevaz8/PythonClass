a=23
b=4
c=4

if b != c:
    b = 1
else:
    c = a
    a = b
    b = c
print(a, b ,c)

# O output foi "4 23 23"