#READING
path = "D:\\Judge\\genome.in"
#path="genome.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])
for i in range(N):
    final=""
    for j in range(len(lines[i])-1, -1, -1):
        if lines[i][j]=="A":
            final+="T"
        elif lines[i][j]=="T":
            final+="A"
        elif lines[i][j]=="G":
            final+="C"
        elif lines[i][j]=="C":
            final+="G"
    print(final)
