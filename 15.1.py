a=1100
print(a)
def testA():
    a=1
    print(a)
def testB():
    global a
    a=200
    print(a)
testA()
testB()
print(a)