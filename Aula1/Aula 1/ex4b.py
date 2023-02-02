a,b,c = map(int, input().split())

if a < 0:
    a = -a
if b < 0:
    b = -b
if c < 0:
    c = -c

if a+b > c and a+c > b and b+c > a:
    if a == b and b == c:
        x = "equilátero"
    if a == b or b == c or c == a:
        x = "isósceles"
    if a != b and b != c and c != a:
        x = "escaleno"
    a = str(a)
    b = str(b)
    c = str(c)
    print("(" + a,b,c + ") definem um triângulo " + x)
else:
    a = str(a)
    b = str(b)
    c = str(c)
    print("(" + a,b,c + ") não definem um triângulo")