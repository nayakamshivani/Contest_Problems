'''integers are given. Find among them the number with minimal sum of digits (in the case if there are some of them with the same sum – print the last number from the input sequence).'''

n=int(input())
a=list(map(int,input().split()))
sum1=9999999999999999999
ans=0
temp=0
for j in range(len(a)):
    f=str(a[j])
    temp=0
    for k in range(len(f)):
        temp=temp+int(f[k])
    if(temp<=sum1):
        sum1=temp
        ans=a[j]
print(ans)
