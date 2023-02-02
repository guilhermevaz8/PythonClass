a, b, c = map(int,input().split())
if b==999 and c==999:
    print("0")
elif b==999:
   print("2")
elif c==999:
   print("1")
elif c==b:
   print("1")
elif abs(c-a)<abs(b-a):
   print("2")
elif abs(c-a)>abs(b-a):
   print("1")
elif abs(c-a)==abs(b-a):
    if c<b:
        print("1")
    else:
        print("2")
