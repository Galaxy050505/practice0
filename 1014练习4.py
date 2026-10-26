"""A=int(input())
line=input().split()
N=0
for s in line:
    num=int(s)
    if num > 0:
        N=num
        break

total=0
for i in range(N):
    total+=A
    A+=1
print(total)
"""
a=int(input())
line=[]
for i in range(1,a+1):
    if a % i==0:
        line.append(i)
        print(i)
