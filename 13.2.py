#plan A
x=int(input('x值'))
y=int(input('y值'))

def add_num1():
    result= x + y
    print(result)
add_num1()
#plan B
def add_num2(a,b):
    result= a + b
    print(result)
x=int(input('x值'))
y=int(input('y值'))
add_num2(x,y)