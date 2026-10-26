""""# 1. 读取行号 L 和 操作符 op
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
print(f"{result:.1f}")"""
"""
z=input().strip()
list1=[]
for i in range(12):
    row =list(map(float,input().strip().split()))
    list1.append(row)#每行加总
total_sum=0.0#初始
count=0#初始
for i in range(12):
    for j in range(12):
        if j>i:
            total_sum += list1[i][j]
            count+=1
if z=='S':
    result = total_sum
else:
    result = total_sum / count
print(f'{result:.1f}')
"""
z=input().strip()
list1=[]
total_sum=0
count=0
for i in range(12):
    row =list(map(float,input().strip().split()))
    list1.append(row)
for i in range(12):
    for j in range(12):
        if j+i<11:
            total_sum += list1[i][j]
            count+=1
if z=='S':
    result = total_sum
else:
    result = total_sum / count
print(f'{result:.1f}')