#if嵌套
money=int(input("Enter your money:"))
seat=int(input("Enter seat:"))
if money>5:
    print('付錢後請上車')
    if seat>0:
        print('上車後請坐下')
    else:
        print('沒座位請站穩')
else:
    print('沒錢不能上車')