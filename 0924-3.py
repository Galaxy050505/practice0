#对列表依次做四个操作：① append 加入新品牌；② remove 去掉 'ducati'；③ pop 弹出末尾元素；④ sort 按字母顺序排序。输出每一步之后的列表。
motor_brands=input().split()
motor_brands_2=input()

brands=[]
brands.extend(motor_brands)
brands.append(motor_brands_2)
print(brands)
brands.remove('ducati')
print(brands)
brands.pop()
print(brands)
brands.sort()
print(brands)

