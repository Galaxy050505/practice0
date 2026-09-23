#99乘法表，多行多個乘法表達式
j=1
while j<=9:
    i=1
    while i <=j:
         print(f'{i}*{j}={i*j}',end='\t')
         i+=1
    print()
    j+=1
#=========
str1='itheima'
for cc in str1:
    if cc=='e':
        continue
    print(cc)
#===========
i=1
while i<=5:
    if i==3:
        break
    print('學習python')
    i+=1
else:
    print('進步了')

#============
i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print('學習python')
    i+=1
else:
    print('進步了')