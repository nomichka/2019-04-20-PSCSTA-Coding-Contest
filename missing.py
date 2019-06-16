#READING
path = "D:\\Judge\\missing.in"
#path="missing.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

for i in range(N):
    lines[i]=lines[i].split()
    start=int(lines[i][0])
    end=int(lines[i][1])
    s=int(lines[i][2])
    total=((end-start+1)*(start+end)/2.0)
    print(int(total-s))
