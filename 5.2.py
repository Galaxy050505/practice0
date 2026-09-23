#多重判斷:年齡是否可工作18-60
age=int(input("Enter your age:"))
if age<18:
    print(f'輸入的年齡是{age},不在工作年齡範圍內,不可工作')
elif 18<=age<=60:
    print(f'輸入的年齡是{age},在工作年齡範圍內,可工作')
elif age>60:
    print(f'輸入的年齡是{age},不在工作年齡範圍內,不可工作')