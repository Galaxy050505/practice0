"""N=int(input())
for i in range(1,10001):
    if i % N == 2:
        print(i)
"""
'''
N=int(input())
count=0
while count <6:
    if N % 2 == 1:
        print(N)
        count+=1
    N+=1
'''
N=int(input())
for i in range(1,11):
    t=i*N
    print(f'{i} x {N} = {t}')