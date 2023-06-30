list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

ans=[]

lngth=min(len(list1), len(list2))

for i in range(lngth):
    ans.append(list1[i])
    ans.append(list2[i])

if len(list1) > lngth:
    ans.extend(list1[lngth:])
elif len(list2) > lngth:
    ans.extend(list2[lngth:])    

print(ans)   