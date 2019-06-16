#READING
path = "D:\\Judge\\robotcommands.in"
#path="robotcommands.in"
fin=open(path, "r")
lines=fin.readlines()
S=int(lines[0])
lines.remove(lines[0])
for i in range(S):
    N=int(lines[i*2])
    lines[i*2+1]=lines[i*2+1].split()
    rl=0
    fb=0
    for element in lines[i*2+1]:
        if element[0]=="R":
            rl+=int(element[1:])
        elif element[0]=="L":
            rl-=int(element[1:])
        elif element[0]=="F":
            fb+=int(element[1:])
        elif element[0]=="B":
            fb-=int(element[1:])
    if fb==0 and rl==0:
        print("YES")
    else:
        print("NO")
