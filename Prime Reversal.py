for i in range(int(input())):
    j , a , b = int(input()) , sorted([int(k) for k in input()]) , sorted([int(k) for k in input()])
    if a == b:
        print('YES')
        continue
    print('NO')
