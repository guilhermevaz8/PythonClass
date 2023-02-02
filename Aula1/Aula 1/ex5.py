a,b,c = map(int, input().split())

if b*b-4*a*c > 0:
    print("A equação tem duas raízes reais.")
if b*b-4*a*c == 0:
    print("A equação tem apenas uma raíz real.")
if b*b-4*a*c < 0:
    print("A equação não tem raízes reais.")