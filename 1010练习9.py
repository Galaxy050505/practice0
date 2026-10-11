a, b, c = map(float, input().split())

# 1. 对边长进行从大到小排序，保证 a 是最大边
a, b, c = sorted([a, b, c], reverse=True)

# 2. 首先判断能否构成三角形
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    # 3. 使用独立的 if (不能用 elif)，因为可能满足多个条件
    # 判断直角、钝角、锐角
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")
    if a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")
    if a ** 2 < b ** 2 + c ** 2:
        print("TRIANGULO ACUTANGULO")

    # 判断等边和等腰
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b or b == c or a == c) and not (a == b and b == c):
        print("TRIANGULO ISOSCELES")