mat=[[1,2,3,4],[5,6,7,8]]
b=[]
for i in mat:
    l=[]
    for j in i:
        if j%2==0:
            l.append(j**3)
        else:
            l.append(j**2)
    b.append(l)
print(b)


i = [[j**3 if j%2==0  else j**2 for j in i]for i in mat] 