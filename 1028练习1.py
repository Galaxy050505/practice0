"""string_row=input()
length=len(string_row)
print(length)
"""""""
s=input()
count=0
for char in s:
    if char.isdigit():
        count+=1
print(count)
"""
from shlex import join

"""
T=int(input())
for i in range(T):
    p1,p2=input().split()
    if p1==p2:
        print('Tie')
    elif (p1,p2) in [('Hunter','Gun'),('Gun','Bear'),('Bear','Hunter')]:
        print('Player1')
    else:
        print('Player2')"""
"""A=input()
print(' '.join(A))"""
A=input()
B=input()
pr=A.replace(B,'#')
print(pr)
