'''Trailing Zeros'''

def Zeros(k): 
    i=5
    count=0
    while(k/i>= 1): 
        count+=int(k/i) 
        i*=5
    print(count)
    return int(count) 
n=int(input())
for i in range(0,n):
    t=int(input())
    Zeros(t)
