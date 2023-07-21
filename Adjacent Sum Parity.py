"""Chef has an array A of length N. Chef forms a binary array B of length N using the parity 
of the sums of adjacent elements in A. Here x%y denotes the remainder obtained when x is divided by y.
Chef lost the array A and needs your help. Given array B, determine whether there exits any valid array A which could have formed B."""

for i in range(int(input())):
    n, s = int(input()), sum(list(map(int,input().split())))
    if s % 2 == 0:
        print('YES')
    else:
        print('NO')
