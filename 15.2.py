glo_num=0

def test1():
    global glo_num
    glo_num=1000
def test2():
    print(glo_num)
test1()
test2()