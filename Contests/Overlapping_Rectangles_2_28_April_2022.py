
'''Overlapping Rectangles'''

t=int(input())
for i in range(0,t):
    l=list(map(int,input().split()))
    x1=l[0]
    y1=l[1]
    x2=l[2]
    y2=l[3]
    m=list(map(int,input().split()))
    x3=m[0]
    y3=m[1]
    x4=m[2]
    y4=m[3]
    
    area1=0
    area2=0
    area3=0
    area1=abs(x2-x1)*abs(y2-y1)
    area2=abs(x4-x3)*abs(y4-y3)
    w=min(x4,x2)-max(x1,x3)
    h=min(y4,y2)-max(y1,y3)
    if(w>0 and h>0):
        area3=w*h
    print(area1+area2-area3)        
    
