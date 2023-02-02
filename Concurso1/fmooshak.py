n=int(input())
soma = 0
maximo = int(input())
minimo = maximo
cmax = cmin = 1
soma += maximo
for k in range(1,n):
    nota = int(input())
    soma += nota
    if nota > maximo:
        maximo = nota
        cmax = 1
    elif nota == maximo:
        cmax += 1
    if nota < minimo:
        minimo = nota
        cmin = 1
    elif nota == minimo:
        cmin += 1
if cmin == 1:
    soma -= minimo
    n -= 1
if cmax == 1:
    soma -= maximo
    n -= 1
print(soma//n)
