C,N=map(int,input().split())
nota1=''
preco=0
linha1=1
while N!=0:
    valor=int(input())
    produto=str(input())
    if valor<=C:
        C-=valor
        preco+=valor
        if linha1==1:
            nota1 = nota1+ produto
        else:
            nota1=nota1 + "\n" + produto
        linha1+=1
    N-=1
if nota1=='':
    print(preco, C)
else:
    print (nota1)
    print(preco, C)
