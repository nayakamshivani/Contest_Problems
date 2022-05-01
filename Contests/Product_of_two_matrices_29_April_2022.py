t=int(input())
for i1 in range(0,t):
    p=list(map(int,input().split()))
    n=p[0]
    m=p[1]
    
    mat1=[]
    mat2=[]
    for i in range(0,n): 
        temp=list(map(int,input().split()))
        mat1.append(temp)
    p1=list(map(int,input().split()))
    n1=p1[0]
    m1=p1[1]


    for j in range(0,n1):
        
        temp1=list(map(int,input().split()))
        mat2.append(temp1)


    mat3=[]
    for i in range(0,n):
        r1=[]
        for j in range(0,m1):
            sum=0
            for k in range(0,n1):
                sum= sum+(mat1[i][k] * mat2[k][j])
                #print(str(mat1[i][j])+" *"+str( mat2[j][k])+" "+str(mat1[i][j+1])+ "*"+str( mat2[j+1][k]))
            r1.append(sum)
        mat3.append(r1)





    for i in range(0,n):
        for j in range(0,m1):
            if(j==m1-1):
                print(mat3[i][j])
            else:
                print(mat3[i][j],end=" ")
         
