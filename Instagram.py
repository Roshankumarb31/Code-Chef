'''Chef categorises an instagram account as spam, if, 
the following count of the account is more than 10 
times the count of followers.Given the following and 
follower count of an account as X and Y respectively,
find whether it is a spam account.'''

for i in range(int(input())):
    m,n = map(int,input().split())
    if m > n*10:
        print('YES')
        continue
    print('NO')
