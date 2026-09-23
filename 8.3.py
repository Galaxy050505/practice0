mystr="hello world and itheima and Python"
print(mystr)
new_str=mystr.lstrip()
print(new_str)
old_str=mystr.rstrip()
print(old_str)
A_str=mystr.strip()
print(A_str)
#lstrip刪除左側空白，rstrip刪除右側空白，strip刪除兩側空白
#ljust左對齊，rjust右對齊，center至中
print(mystr.startswith('hello'))
print(mystr.endswith('n'))
print(mystr.isalpha())#全字母(空格不是字母)
print(mystr.isdigit())#數字
print(mystr.isalnum())#數字或字母組合(例如abc123)
print(mystr.isspace())#空白