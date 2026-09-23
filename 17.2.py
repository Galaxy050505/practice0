#用示例來展現lambda的區別
#a+b 函數實現
def add(a,b):
    return a+b
result=add(3,4)
print(result)


#a+b lambda實現
fn1=lambda a,b:a+b
print(fn1(3,4))
