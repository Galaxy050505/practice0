#读入一个首尾带空白（空格或制表符）的名字，分别输出去掉左侧、右侧、两侧空白后的结果。为了让空白“看得见”，输出时用方括号把结果括起来。


name=input()
print(f'[{name.lstrip()}]')
print(f'[{name.rstrip()}]')
print(f'[{name.strip()}]')