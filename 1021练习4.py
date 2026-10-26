"""while True:
    N=int(input())
    if N==0:
        break
    for i in range(N):
        for j in range(N):
            val=str(min(i,j,N-1-i,N-1-j)+1)
            if j==N-1:
                print(val)
            else:
                print(val,end=' ')


    print()# 外层 for 循环结束，说明当前这个 N 阶矩阵打印完了，题目要求矩阵之间要有一个空行
    # 核心公式：计算当前位置(i, j)距离上下左右四条边的最短距离，再 +1。
    # i 是距离上边界的距离
    # N - 1 - i 是距离下边界的距离
    # j 是距离左边界的距离
    # N - 1 - j 是距离右边界的距离
    # 将这些值转为字符串，方便后续直接 print"""
list1=[]
for i in range(20):
    x=int(input())
    list1.append(x)
reversed_list=list1[::-1]
for i in range(20):
    print(f'N[{i}] = {reversed_list[i]}')
