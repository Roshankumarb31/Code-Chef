"""Chef is fan of pairs and he likes all things that come in pairs. He even has a doll collection in which the dolls come in pairs. 
One day while going through his collection he found that there are odd number of dolls. Someone had stolen a doll!!!

Help chef find which type of doll is missing.."""

for i in range(int(input())):
    l, d = [], {}
    n = int(input())
    for j in range(n):
        t = int(input())
        l.append(t)
    for x in l:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    for k in d:
        if d[k] % 2 != 0:
            print(k)
