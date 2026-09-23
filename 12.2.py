dict1={i:i**2 for i in range(1,5)}
print(dict1)
list1=['name','age','gender']
list2=['TOM',20,'man']
dict2={list1[i]:list2[i] for i in range(len(list1))}
print(dict2)