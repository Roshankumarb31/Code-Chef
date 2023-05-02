for i in range(int(input())):
    j = int(input())
    a = [int(k) for k in input()]
    b = [int(k) for k in input()]
    a.sort()
    b.sort()
    if a == b:
        print('YES')
        continue
    print('NO')
