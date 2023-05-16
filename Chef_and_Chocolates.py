'''Chef has X 5 rupee coins and Y 10 rupee coins. 
Chef goes to a shop to buy chocolates for Chefina 
where  each  chocolate  costs  Z  rupees.  Find
the maximum number of chocolates that Chef can buy
for Chefina.'''


for i in range(int(input())):
    f,s,n = map(int,input().split())
    x = f*5 + s*10
    if x > n:
        print(x//n)
        continue
    print(0)
