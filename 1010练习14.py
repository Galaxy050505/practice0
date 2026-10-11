import math

# 1. 读取一行输入，按空格切分并转换为浮点数
a, b, c = map(float, input().split())

# 2. 情况一：a 为 0，不是二次方程
if a == 0:
    print("Impossivel calcular")
else:
    # 计算判别式 delta = b^2 - 4ac
    delta = b ** 2 - 4 * a * c

    # 3. 情况二：判别式 < 0，无实数根，输出共轭复根
    if delta < 0:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-delta) / (2 * a)  # 根据题目提示，a为负数时虚部算出来就是负的，不取绝对值

        # 严格按照题目要求的格式输出
        print(f"x1={real_part:.5f}+{imag_part:.5f}i;x2={real_part:.5f}-{imag_part:.5f}i")

    # 4. 情况三：判别式 >= 0，输出两个实数根
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)

        # 题目要求“较大的根为 x1，较小的为 x2”
        # 因为 a 可能是负数，所以不能默认 + 出来的就是大根，需要显式比较大小
        if x1 < x2:
            x1, x2 = x2, x1

        print(f"x1={x1:.5f};x2={x2:.5f}")