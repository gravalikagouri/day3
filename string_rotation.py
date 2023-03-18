str1 = input().split(",")
string = []
digit = []
for i in str1:
    s1,n = i.split(":")
    string.append(s1)
    digit.append(n)
def rotate(ss,n1):
    n1 = str(n1)
    s =0
    for i in n1:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(digit)):
    print(rotate(string[i],digit[i]))