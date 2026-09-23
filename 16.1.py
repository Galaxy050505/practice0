a=1
b=a

print(b)

print(id(a))
print(id(b))

a=2
print(b)
print(id(a))
print(id(b))

aa=[10,20]
bb=aa
print(bb)

print(id(aa))
print(id(bb))
aa.append(30)
print(aa)
print(bb)
#因為列表是可修改類型
print(id(aa))
print(id(bb))