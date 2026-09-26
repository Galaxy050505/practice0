#读入一个人的名字（全小写英文字母），分别输出它的全小写、全大写、首字母大写三种形式。这是字符串最基本的三个方法：lower()、upper()、title()。
name=input()
print(name.lower())
print(name.upper())
print(name.title())

#把 4 个自行车品牌读进一个列表，输出列表的第一个和最后一个品牌（首字母大写）。列表索引从 0 开始；-1 表示最后一个元素，不用先求长度。
n1=input()
n2=input()
n3=input()
n4=input()
brands=[n1,n2,n3,n4]
print(brands[0].title(),brands[-1].title())
#一行输出
brands=input().split()
print(brands[0].title(),brands[-1].title())