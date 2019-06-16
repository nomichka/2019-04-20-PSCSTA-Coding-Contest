#READING
path = "D:\\Judge\\knight.in"
#path="knight.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])
alpha="ABCDEFGH"
stuff=[[-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1]]
for i in range(N):  
    lines[i]=lines[i].split()
    a=[alpha.index(lines[i][0][0]), int(lines[i][0][1])-1]
    b=[alpha.index(lines[i][1][0]), int(lines[i][1][1])-1]
    c=[alpha.index(lines[i][2][0]), int(lines[i][2][1])-1]
    going=True
    for al in range(8):
        for n in range(8):
            foundOne=0
            for l in [a, b, c]:
                
                for pos in stuff:
                    if al+pos[0]==l[0] and n+pos[1]==l[1]:
                        foundOne+=1
                if foundOne==3 and going:
                    going=False
                    print(alpha[al]+str(n+1))
                    break
                
    """
    poss=[]
    if a[0]==b[0]:
        new1=alpha[alpha.index(a[0])+1] + str((a[1]+b[1])/2)
        new2=alpha[alpha.index(a[0])-1] + str((a[1]+b[1])/2)
        poss.append(new1)
        poss.append(new2)
    elif abs(alpha.index(a[0])-alpha.index(b[0]))==2:
        new1=alpha[(alpha.index(a[0])+alpha.index(b[0]))/2] + str(a[1])+2
        new2=alpha[(alpha.index(a[0])+alpha.index(b[0]))/2] + str(a[1])-2
        poss.append(new1)
        poss.append(new2)
    elif a[1]==b[1]:
        new1=alpha[(alpha.index(a[0])+alpha.index(b[0]))/2] + str((a[1])+1)
        new2=alpha[(alpha.index(a[0])+alpha.index(b[0]))/2] + str((a[1])+1)
        poss.append(new1)
        poss.append(new2)
    elif a[
    """        
