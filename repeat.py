#READING
path = "D:\\Judge\\repeat.in"

#path="repeat.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

a=""
for i in range(N):
    lines[i]=lines[i].split()
    b=""
    for j in range(int(lines[i][1])):
        b+=lines[i][0]+" "
    a+=b+"\n"

print(a)









