"""A=input()
char_count={}
for char in A:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
    found=False
for char in A:
    if char_count[char]==1:
        found=True
        print(char)
        break
if not found:
    print('no')""""""
k=float(input())
a=input().strip()
b=input().strip()
count=0
len_a=len(a)
for i in range(len_a):
    if a[i]==b[i]:
        count+=1
if (count/len_a)>k:
    print('yes')
else:
    print('no')""""""
a=input().upper()
b=input().upper()
count={}
if a==b:
    print('=')
elif a>b:
    print('>')
else:
    print('<')"""
a=input()
print(' '.join(a.split()))