listaOutput=[]

numNos,numRamos=map(int,input().split())
infoRamos={}
for i in range(numRamos):
    descricaoRamo= list(map(int,input().split()))
    infoRamos[(descricaoRamo[0],descricaoRamo[1])]= descricaoRamo[2]
    infoRamos[(descricaoRamo[1],descricaoRamo[0])]= descricaoRamo[2]

descricaoTrajeto=list(map(int,input().split()))
while descricaoTrajeto[0]!=0:
    tempMax=infoRamos[(descricaoTrajeto[1],descricaoTrajeto[2])]
    tempMin=tempMax
    for k in range(2,descricaoTrajeto[0]):
        if tempMax>infoRamos[(descricaoTrajeto[k],descricaoTrajeto[k+1])]:
            tempMin=infoRamos[(descricaoTrajeto[k],descricaoTrajeto[k+1])]
        elif tempMax < infoRamos[(descricaoTrajeto[k],descricaoTrajeto[k+1])]:
            tempMax=infoRamos[(descricaoTrajeto[k],descricaoTrajeto[k+1])]
    listaOutput.append("%d %d" %(tempMin, tempMax))
    descricaoTrajeto=list(map(int,input().split()))
for x in range (len(listaOutput)):
    print(listaOutput[x])
