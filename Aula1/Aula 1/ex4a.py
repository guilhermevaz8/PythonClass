a,b,c = map(int, input().split())

if a < 0:
    a = -a
if b < 0:
    b = -b
if c < 0:
    c = -c

if a+b > c and a+c > b and b+c > a:
    a = str(a)
    b = str(b)
    c = str(c)
    print("(" + a,b,c + ") definem um triângulo")
else:
    a = str(a)
    b = str(b)
    c = str(c)
    print("(" + a,b,c + ") não definem um triângulo")