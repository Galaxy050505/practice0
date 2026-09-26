#输入一个整数 N 和一个长度为 N 的整数数组 X。请你找到数组中最小的元素，并输出它的值和下标。注意，如果有多个最小值，则返回下标最小的那个。
#提示：min() 和 list.index() 可以帮你免写循环。
"""
输入
第一行包含整数 N。第二行包含 N 个用空格隔开的整数 X[i]。数据范围：1 < N ≤ 1000，-1000 < X[i] ≤ 1000
输出
第一行输出 Minimum value: x，第二行输出 Position: y（下标从 0 开始）。
"""


N = int(input())
X = list(map(int, input().split()))

min_val = min(X)#min(X)：调用 Python 内置函数 min()，返回列表 X 中的最小值，把最小值保存到变量 min_val
min_index = X.index(min_val)#.index() 是列表的一个方法，作用是：查找某个值在列表中第一次出现的位置（下标）。

print("Minimum value:", min_val)
print("Position:", min_index)
