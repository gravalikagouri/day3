sentences =["a new world record was set",
    "in the holy city of ayodha",
    "on the eve of diwali on tuesday",
    "with over three lakh diya or earthen lamps",
    "lit up simu on the banks of saryu river"]
stopwards =['for','a','of','the','and','to','in','on','with','was']
res = []
for sentence in sentences:
    row=[]
    for word in sentence.split():
        if word not in stopwards:
            row.append(word)
    res.append(row)
print(res)
print([word for word in sentence])
# print([[word for word in sentences.split() if word not in stopwards] for sentence in sentence])

       