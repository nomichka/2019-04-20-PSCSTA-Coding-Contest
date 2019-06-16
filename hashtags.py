#READING
path = "D:\\Judge\\hashtags.in"
#path="hashtags.in"
fin=open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])
for i in range(N):
    final=""
    words=lines[i].split()
    for w in words:
        if "#" in w:
            added=False
            for j in range(1, len(w)):
                l=w[j]
                if l in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
                    final+=l
                    added=True
                elif l in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
                    final+=l
                    added=True
                else:
                    break
            if added:
                final+=" "
    print(final)
