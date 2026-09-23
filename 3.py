#檢測數據類型--type(數據)
#int--type整數型
num1=1
#float--type浮點數型
num2=1.1
print(type(num1))
print(type(num2))
#string--type字符串型(數據都要帶引號)
a='hello world'
print(type(a))
#bool--布爾型'判斷時使用,有兩個取值'(True or False)
b=True
print(type(b))
#list--type列表類型[]
c=[10,20,30]
print(type(c))
#tuple--type元組類型()
d=(10,20,30)
print(type(d))
#set--type集合類型{}
e={10,20,30}
print(type(e))
#dict--type字典類型--鍵值對
f={'name':'TOM','age':18}
print(type(f))
#==============
#轉換數據類型
#input()輸入皆是字符串類型,需轉換類型
num=(input('請輸入數字'))
print(num)
print(type(num))#此處數據類型為string字符串
print(type(int(num)))#int
#==============
#float()--轉浮點數
num1=1
str1='10'
print(type(float(num1)))
float(num1)
float(str1)
#str()--轉字符串

#tuple()--轉元組

#list()--轉列表

#eval()--計算在字符串中有效的python表達式並返回一一對象