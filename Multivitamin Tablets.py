"""The doctor prescribed Chef to take a multivitamin tablet 3 times a day for the next X days.
Chef already has Y multivitamin tablets.Determine if Chef has enough tablets for these X days or not."""

for i in range(int(input())):
    a,b = map(int,input().split())
    if a*3 <= b:
        print('YES')
    else:
        print('NO')
