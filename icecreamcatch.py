#READING
path = "D:\\Judge\\icecreamcatch.in"
#path="icecreamcatch.in"
fin=open(path, "r")
lines=fin.readlines()
S=int(lines[0])
lines.remove(lines[0])
start=0
end=0
for i in range(S):
    N=int(lines[start])
    end+=N+1
    mini=1000
    maxi=0
    for j in range(start+1, end):
        lines[j]=lines[j].split()
        mini=min(int(lines[j][0]), mini)
        maxi=max(int(lines[j][1]), maxi)
    print(mini, maxi, str(maxi-mini+1))
    start+=N+1
