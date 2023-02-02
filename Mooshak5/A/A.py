n=int(input())
hora=0
min=8
imp=0
max=18
a,b=map(int,input().split())
while n!=0:
    if a>max or b<min:
        print('impossivel')
        imp+=1
        n=0
    else:
        if a>min:
            min=a
        if b<max:
            max=b
        n-=1
        if n!=0:
            a, b = map(int, input().split())
if imp==0:
    if (max-min)%2!=0:
        hora=((max-min)//2)+min
        print('%d e meia' %hora)
    else:
        hora=((max-min)//2)+min
        print(hora)



