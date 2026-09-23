#5/30函數嵌套
def testB():
    print('B start')
    print('B函數')
    print('B end')

def testA():
    print('A start')
    testB()
    print('A end')
testA() 