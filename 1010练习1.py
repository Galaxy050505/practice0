"""
a,b=map(int,input().split())
if a!=0 and b!=0 and a%b == 0 or b%a == 0:
    print("Y")
else:
    print("N")
"""
menu={
1: 4.00,
2: 4.50,
3: 5.00,
4: 2.00,
5: 1.50,}
x,y=map(int,input().split())
price=menu[x]
total=price*y
print(f'Total: R$ {total:.2f}')
