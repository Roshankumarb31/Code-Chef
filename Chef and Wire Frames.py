"""Chef has a rectangular plate of length Ncm and width Mcm. He wants to make 
a wireframe around the plate. The wireframe costs X rupees per cm. 
Determine the cost Chef needs to incur to buy the wireframe."""


for i in range(int(input())):
    a, b, c = map(int,input().split())
    print(((a*2)+(b*2))*c)
