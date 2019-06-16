#READING
path = "D:\\Judge\\dewey.in"
#path="dewey.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

def my_function(entry):
    return (entry[2], entry[0], entry[1])
for i in range(N):
    lines[i]=lines[i].split()
    num=int(lines[i][0])
    lines[i].remove(lines[i][0])
    words=sorted(lines[i], key=my_function)
    a=""
    for word in words:
        a+=word+ " "
    print(a)
