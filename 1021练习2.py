"""L=int(input()).strip())
z=input().strip()
for i in range(12):
    if z=s:

    elif z=m:

    else:
        break
"""
# 1. 读取行号 L 和 操作符 op
L = int(input().strip())
op = input().strip()

target_row = []

# 2. 遍历读取 12 行数据
for i in range(12):
    # 读取一行并按空格分割成列表，转换为浮点数
    row = list(map(float, input().strip().split()))
    # 如果当前行号等于目标行号，保存这一行
    if i == L:
        target_row = row

# 3. 计算结果
total_sum = sum(target_row)

if op == 'S':
    result = total_sum
else:  # op == 'M'
    result = total_sum / 12.0

# 4. 输出结果，保留一位小数
print(f"{result:.1f}")