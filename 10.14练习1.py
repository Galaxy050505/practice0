"""number=1
while True:
    if number>100:
        break
    if number%2==0:
        print(number)
    number=number+1
""""""
Max=int(input())
for i in range(1,Max+1):
    if i <Max+1 and i%2==1:
        print(i)
    i+=1
"""
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
count=0
if a>0:
    count+=1
if b>0:
    count+=1
if c>0:
    count+=1
if d>0:
    count+=1
if e>0:
    count+=1
if f>0:
    count+=1
print(f'{count} positive numbers')
