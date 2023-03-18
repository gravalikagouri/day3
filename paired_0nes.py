my_list = [9,3,6,1,5,0,8,2,4,7]
l_b = [6,4,6,1,2,2]
# m={}
# for i in l_b:
#     if i in my_list:
#         m[i]=my_list.index(i)
# print(m)
# l = [(i, my_list.index(i)) for i in l_b]
# print(dict(l))
# l1 = [{i: my_list.index(i) for i in l_b}]
# print(l1)
r = []
for i in l_b:
    if i in my_list:
        r.append((i,my_list.index(i)))
print(r)
