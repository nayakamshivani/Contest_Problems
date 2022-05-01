t=int(input())
for t1 in range(0,t):
    flag=0
    s=input()
    dict1={}
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if(s[i]==s[j]):
                flag=1
                print(s[i])
                break
        if(flag==1):
            break
    if(flag!=1):
        print('.')
        
        
