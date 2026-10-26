"""a,b=map(int,input().split())
list1=[]
if a>b:
    a,b=b,a
for i in range(a+1,b):
    if i%2==1:
        list1.append(i)
print(sum(list1))
"""
Max=int(input())
nums=[]
while len(nums)<Max:
    nums.extend(list(map(int,input().split())))
    nums=nums[:Max]
max_val=nums[0]
max_pos=1
for i in range(1,Max):
    if nums[i]>max_val:
        max_val=nums[i]
        max_pos=i+1
print(max_val)
print(max_pos)
