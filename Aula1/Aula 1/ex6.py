a,b = map(int, input().split())

if a != 0:
    if b !=0:
        if a//b == a/b and a%b == 0:
            print("sim")
        else:
            print("nao")
    else:
        print("nao")
else:
    print("nao")