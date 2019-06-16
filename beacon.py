#READING
path = "D:\\Judge\\beacon.in"
#path="beacon.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

for i in range(N):
    lines[i]=lines[i].split()
    lines[i][0]=int(lines[i][0])
    lines[i][1]=int(lines[i][1])
    length=1
    direction="r"
    loc=[0, 0]
    going=True
    if lines[i]==loc:
        print(0)
        going=False
    total=0
    directions="ruld"
    n=0
    while going:
        if direction=="r":
            for j in range(length):
                loc[0]+=1
                total+=1
                if loc==lines[i]:
                    print(total)
                    going=False
        elif direction=="l":
            for j in range(length):
                loc[0]-=1
                total+=1
                if loc==lines[i]:
                    print(total)
                    going=False
        elif direction=="u":
            for j in range(length):
                loc[1]+=1
                total+=1
                if loc==lines[i]:
                    print(total)
                    going=False
        elif direction=="d":
            for j in range(length):
                loc[1]-=1
                total+=1
                if loc==lines[i]:
                    print(total)
                    going=False
        direction=directions[(directions.index(direction)+1)%4]
        n+=1
        if n%2==0:
            length+=1
    






                    
