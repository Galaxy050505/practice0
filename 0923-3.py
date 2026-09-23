"""
读取四个整数 A、B、C、D，计算 A×B − C×D。
一行，四个整数 A、B、C、D，用空格隔开。
"""
a,b,c,d=map(int, input().split())
print(f"answer={a*b-c*d}")