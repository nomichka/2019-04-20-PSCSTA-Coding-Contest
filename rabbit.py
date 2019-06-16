#READING
path = "D:\\Judge\\rabbit.in"
#path="rabbit.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

a=""
for i in range(N):
    lines[i]=lines[i].split()
    current=1
    amount=0
    for element in lines[i]:
        current+=int(element)
        if current%2==0:
            amount+=1
    a+=str(amount)+"\n"
print(a)
