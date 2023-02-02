a, m, d = map(int,input().split())
if m<3:
   a=a-1
   m=m+12
A=a//100
B=A//4
if (a==1582 and m==10 and d>15) or (m>10 and a==1582) or a>1582:
   C=2-A+B
if (a<=1582 and m<=10 and d<=4) or (m<=10 and a<=1582) or a<1582:
   C=0
D=(int)(365.25*(a+4716))
E=(int)(30.6001*(m+1))
J=D+E+d+C-1524
print(J)
