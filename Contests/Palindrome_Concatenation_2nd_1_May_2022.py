t=int(input())
for t1 in range(0,t):
    l=input().split()
    a=l[0]
    b=l[1]
    flag=0
    b=list(b)
    b=set(b)
    for i in range(0,len(a)):
        if(a[i] in b):
            flag=1
            print("Yes")
            break
    if(flag==0):
        print("No")
        
        
