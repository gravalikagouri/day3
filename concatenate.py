a = list(map(int,input().split(",")))
num1 = (sum(a[:a.index(5)])+sum(a[a.index(8)+1:]))
l = a[a.index(5):a.index(8)+1]
num2=""
for i in l:
    num2+=str(i)
print(int(num2)+num1)
