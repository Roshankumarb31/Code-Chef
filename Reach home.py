'''Chef is hungry and wants to reach home.

Chef can travel up to 5 kilometres on 1 litre of fuel on his motorcycle.
Currently, his motorcycle is filled with X litres of fuel and his home is 
Y kilometres away.

Determine whether Chef can reach his home on his motorcycle or not.'''


for i in range(int(input())):
    a,b = map(int,input().split())
    if a*5 < b:
        print('NO')
        continue
    print('YES')
