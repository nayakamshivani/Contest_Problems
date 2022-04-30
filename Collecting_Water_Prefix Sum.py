#You are given the heights of N buildings. All the buildings are of width 1 and are adjacent to each other with no empty space in between.
#Assume that its raining heavily, and as such water will be accumulated on top of certain buildings.
#Your task is to find the total amount of water accumulated

t=int(input())
for t1 in range(0,t):
    n=int(input())
    l=list(map(int,input().split()))
    
    ps=[0 for i in range(0,len(l))]
    ss=[0 for i in range(0,len(l))]
    res=[0 for i in range(0,len(l))]
    max=l[0]
    ps[0]=l[0]
    for i in range(1,len(l)):
        if(max>=l[i]):
            ps[i]=max
        elif(max<l[i]):
            max=l[i]
            ps[i]=max
    n=n-1
    max1=l[n]
    ss[0]=l[n]
    for i in range(n,-1,-1):
        if(max1>=l[i]):
            ss[i]=max1
        elif(max1<l[i]):
            max1=l[i]
            ss[i]=max1
    for i in range(0,n+1):
        res[i]=min(ps[i],ss[i])-l[i]
    
    SumRes=0
    for i in range(0,len(res)):
        SumRes=SumRes+res[i]
    print(SumRes)
        
