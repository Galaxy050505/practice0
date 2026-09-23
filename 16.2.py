def test1(a):
    print(a)
    print(id(a))
    a+=a
    print(a)
    print(id(a))

b=100
test1(b)

c=[11,22]
test1(c)

"""
總結:
可變類型:列表、字典、集合
不可變類型:整型、浮點型、字符串、元組
"""