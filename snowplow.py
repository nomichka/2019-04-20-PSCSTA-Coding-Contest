#READING
path = "D:\\Judge\\snowplow.in"
#path="snowplow.in"
fin=open(path, "r")
lines=fin.readlines()
S=int(lines[0])
lines.remove(lines[0])
start=0
end=0
for i in range(S):
    N=int(lines[start])
    end+=N+1
    grid=[[".", ".", "."], [".", ".", "."]]
    for j in range(start+1, end):
        grid.append(lines[j])
    moves=0
    loc=[0, 0]
    passed=True
    while loc[1]!=N:
        if loc[0]==0 and grid[loc[1]+2][loc[0]]!="x" and grid[loc[1]+2][loc[0]+1]!="x":
            loc[1]+=1
        elif loc[0]==1 and grid[loc[1]+2][loc[0]]!="x" and grid[loc[1]+2][loc[0]+1]!="x":
            loc[1]+=1
        elif loc[0]==0 and grid[loc[1]][loc[0]+2]!="x" and grid[loc[1]+1][loc[0]+2]!="x":
            loc[0]+=1                
        elif loc[0]==1 and grid[loc[1]][loc[0]-1]!="x" and grid[loc[1]+1][loc[0]-1]!="x":
            loc[0]-=1
        else:
            loc[1]=N
            passed=False
            break
        moves+=1
    if passed:
        print("YES " + str(moves))
    else:
        print("NO")



    start+=N+1
