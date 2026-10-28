s = input()
a = input()
b = input()

# 按空格拆分单词
words = s.split()

# 遍历单词列表，如果是 a 就换成 b，否则保持不变
# 列表推导式一步到位
new_words = [b if word == a else word for word in words]

# 用空格重新拼接并输出
print(' '.join(new_words))