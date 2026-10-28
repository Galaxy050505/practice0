# 1. 读取输入
n, m = map(int, input().split())

# 2. 创建 n 行 m 列的全 0 矩阵
matrix = [[0] * m for _ in range(n)]

# 3. 定义四个方向的坐标偏移量：右(0,1)、下(1,0)、左(0,-1)、上(-1,0)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 4. 初始化
r, c = 0, 0  # 当前所在的行和列
d = 0  # 当前的朝向（0代表向右）
num = 1  # 要填的数字，从1开始

# 5. 开始填数字
while num <= n * m:
    matrix[r][c] = num  # 填数
    num += 1  # 数字加1

    # 计算下一个位置
    nr = r + dr[d]
    nc = c + dc[d]

    # 检查下一个位置是否合法（没越界，且没被填过）
    if nr < 0 or nr >= n or nc < 0 or nc >= m or matrix[nr][nc] != 0:
        # 如果不合法，顺时针换方向
        d = (d + 1) % 4
        # 重新计算一下换方向后的下一个位置
        nr = r + dr[d]
        nc = c + dc[d]

    # 移动到下一个位置
    r, c = nr, nc

# 6. 打印矩阵
for i in range(n):
    # 使用 * 解包打印，自带空格分隔，最简单优雅
    print(*matrix[i])

# 7. 题目要求最后再输出一个空行
print()