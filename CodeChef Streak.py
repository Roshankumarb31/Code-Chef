"""CodeChef offers a feature called streak count. A streak is maintained if you solve at least one problem daily.

Om and Addy actively maintain their streaks on CodeChef. Over a span of 

N consecutive days, you have observed the count of problems solved by each of them.

Your task is to determine the maximum streak achieved by Om and Addy and find who had the longer maximum streak."""

for i in range(int(input())):
    n, a, b, al, bl, ac, bc = int(input()), list(map(int,input().split())), list(map(int,input().split())), [], [], 0, 0
    for j in range(n):
        if a[j] == 0:
            al.append(ac)
            ac = 0
        if b[j] == 0:
            bl.append(bc)
            bc = 0
        if a[j] !=0:
            ac += 1
        if b[j] != 0:
            bc += 1
    al.append(ac)
    bl.append(bc)
    at, bt = max(al), max(bl)
    if at == bt:
        print('Draw')
    elif at > bt:
        print('Om')
    else:
        print('Addy')
