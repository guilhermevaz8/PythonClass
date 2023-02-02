patassom=str(input())
som=patassom[2:]
patas=patassom[0]
countjacomin=0
countjacomax=0
total=0
while patassom!='0':
    som = patassom[2:]
    patas = patassom[0]
    if patas=='2':
        countjacomax+=1
        if (som!='piupiu' and som!='cocorocoo' and som!= 'cacaraca' and som!='quaqua'):
            countjacomin+=1
    total+=1
    patassom=str(input())
print(total,countjacomin,countjacomax)