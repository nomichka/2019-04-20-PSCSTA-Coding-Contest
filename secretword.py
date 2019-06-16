#READING
path = "D:\\Judge\\secretword.in"
#path="secretword.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])
for i in range(N):
    num=int(lines[i*2])
    words=lines[i*2+1].split()
    final=""
    for j in range(num):
        if len(words[j])>j:
            final+=words[j][len(words[j])-1-j]
    print(final)
