# 1. 读取输入，按空格切分并转换为整数列表
nums = list(map(int, input().split()))

# 2. 使用 sorted() 获取一个排序后的新列表
# 注意：不要用 nums.sort()，那样会改变原列表 nums 的顺序
sorted_nums = sorted(nums)

# 3. 升序输出（每行一个）
for n in sorted_nums:
    print(n)

# 4. 输出一个空行
print()

# 5. 按原输入顺序输出（每行一个）
for n in nums:
    print(n)
