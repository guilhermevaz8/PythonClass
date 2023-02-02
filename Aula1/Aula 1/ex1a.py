a=23
b=4
c=4

if b == c:
    b=1
if c == 1:
    a = b
    b = a
    c = 0
print(a, b, c)

#O output deu "23 1 4"