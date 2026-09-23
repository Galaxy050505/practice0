mystr='hello world and itcast and itheima and Python'
new_str=mystr.replace('and','he',10)
print(mystr)
print(new_str)
new1_str=mystr.split('and',2)
print(new1_str)
mylist=['1','2','3']
new_str='...'.join(mylist)
print(new_str)
old_str=mystr.title()
print(old_str)
#title():每個單詞首字母大寫
A_str=mystr.upper()
print(A_str)
#upper():小寫轉大寫
B_str=mystr.lower()
print(B_str)
#lower():大寫轉小寫