"""N=int(input())
list1=list(map(int,input().split(' ')))
min_list=min(list1)
list1.index(min_list)
print('Minimum value:',min_list)
print('Position:',list1.index(min_list))"""
C=int(input())
test=input()
total_count=0
for i in range(12):
    listx=list(map(float,input().split(' ')))
    total_count+=listx[C]

if test=='S':
    print(f'{total_count:.1f}')
elif test=='M':
    total_count=total_count/12
    print(f'{total_count:.1f}')

