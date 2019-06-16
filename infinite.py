#READING
path = "D:\\Judge\\infinite.in"
#path="infinite.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])
threes=[]
a=1
b=2
for i in range(2, 2000):
    threes.append(a)
    threes.append(b)
    a+=i
    b+=i
for i in range(N):
    if int(lines[i])==1:
        print(2)
    elif int(lines[i]) in threes:
        print(3)
    else:
        print(4)
