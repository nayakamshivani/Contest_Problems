

'''Starting from point (0,0) on a plane, we have written all non-negative integers
0, 1, 2,... as shown in the figure. For example, 1, 2, and 3 has been written at points (1,1), (2,0), and (3, 1) respectively and this pattern has continued.'''

 

t=int(input())
for i in range(0,t):
    l=list(map(int,input().split()))
    n1=l[0]
    n2=l[1]
    if(n1==0 and n2==0):
        print(0)
    
    elif(n1%2==0 and n2%2==0):
        if(n1<n2 or n1-n2>2):
            print("No Number")
        else:
            print(n1+n2)
    elif(n1%2!=0 and n2%2!=0):
        if(n1<n2 or n1-n2>2):
             print("No Number")
        else:
            print((n1+n2)-1)
    else:
        print("No Number")
