# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
888
13.14
"一一一"
"""
多行注釋
"""
#寫一個整數字面量
print(888)
#寫一個浮點數字面量
print(13.14)
#寫一個字符串字面量
print("一一一")
#初始錢
money=50
#花費
蛋糕=10
飲料=5
餘額=money-蛋糕-飲料
print(餘額)
#方法1
print(type('老鼠愛大米'))
print(type(666))
print(type(13.14))
#方法2
string_type=type('老鼠愛大米')
int_type=type(666)
float_type=type(13.14)
print(string_type)
print(int_type)
print(float_type)
#方法3
name='老鼠'
name_type=type(name)
print(name_type)
#轉換
num_str=str(11)
print(type(num_str),num_str)
float_str=str(1.1)
print(type(float_str),float_str)
num=int('11')
print(type(num),num)
num2=float(1.1)
print(type(num2),num2)
float_num=float(11)
print(type(float_num),float_num)
int_num=int(11.11)
print(type(int_num),int_num)


#新
name="張三"
print(name)
#算數
print('1+1=',1+1)
print('2-1=',2-1)
print('3*3=',3*3)
print('4/2=',4/2)
#取整除
print('11//2=',11//2)
print('9%2=',9%2)
print('2**2=',2**2)
#複合算數
number=1+2*3
#複合賦值運算
num=1
num+=1
print('num+=1:',num)
num-=1
print('num-=1:',num)
num*=4
print('num*=4:',num)
num/=2
print('num/=2:',num)
num=3
num%=2
print('num%=2:',num)
num**=2
print('num**=2:',num)
num=9
num//=2
print('num//2:',num)
#單引號
name='老鼠'
print(name)
name1="老鼠1"
print(name1)
name2="""老鼠2"""
print(name2)
name='"新的老鼠"'
print(name)
#字符串拼接
print('學python'+'加油!')
name='老鼠'
address='地球村'
tel=10086
tel_str=str(10086)
print('我是'+name+'我的地址是'+address+str(10086))
#佔位拼接
name='老鼠'
message='學python %s' %name
print(message)
class_num=66
avg_salary=10000
message='數據分析,第%s期平均%s'%(class_num,avg_salary)
print(message)
name='老鼠'
year=20
price=100
message= '我是%s,今年%d歲,價格是%f' %(name,year,price)
print(message)
num1=11
num2=11.345
print('數字11寬度設置5,結果是%5d'% num1)
print('數字11寬度設置1,結果是%1d'% num1)
print('數字11.345寬度設置為7,小數精度2,結果是%7.2f'% num2)
print('數字11.3451寬度不限制,小數精度2,結果是%.2f'% num2)
name='老鼠'
bornyear=1900
price=100
print(f'我是{name}出生於{bornyear}現在價值{price} ')
print('%d'%(1*1))
print(f'{1*1}')
print('類型%s'% type('字符串'))
goodname='橙子'
price=19.99
good_num=1008
price_growth=1.2
sevendaylaterprice=19.99*1.2**7
print('產品%s'%goodname)
print('編號%d'%good_num)
print('價格%.2f'%price)
print('增長%.2f'%price_growth)
print('七天後價格%.2f'%sevendaylaterprice)
name99=input('請告訴我你是誰')
print('我是%s'%name99)
#輸入數字類型
num=input('告訴我你的號碼')
#字串轉數據
num=int(num)
print('num%s'%num,type(num))