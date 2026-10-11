lista=[1,4,6,2,5,7,4,2,8,3,1]#11个数字
sorted_list=sorted(lista)
sum_list=sum(lista)
print(sum_list)
listb=list(dict.fromkeys(lista))
print(f'无重复:{listb}')
print(sorted_list[9])