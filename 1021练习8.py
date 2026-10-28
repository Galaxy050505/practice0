test=input()
total_count=0
count=0
for i in range(12):
    list1 = list(map(float, input().split()))
    for j in range(12):
        if i+j>11:
            total_count+=list1[j]
            count+=1

if test=='S':
    print(f'{total_count:.1f}')
elif test=='M':
    print(f'{total_count/count:.1f}')
