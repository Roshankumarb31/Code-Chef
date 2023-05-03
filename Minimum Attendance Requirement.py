for i in range(int(input())):
    j, c = int(input()), 0
    for k in [int(l) for l in input()]:
        if k == 0:
            c += 1
    c = 120 - c
    if c/120 >= 0.75:
        print('YES')
        continue
    print('NO')
