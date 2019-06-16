#READING
path = "D:\\Judge\\abcwords.in"
#path="abcwords.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
for i in range(N):
    value=0
    good=True
    for j in range(len(lines[i])):
        if letters.index(lines[i][j])>=value:
            value=letters.index(lines[i][j])
        else:
            good=False
    if good:
        print("YES")
    else:
        print("NO")
