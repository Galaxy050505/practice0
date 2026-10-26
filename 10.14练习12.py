t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11)
even = 0
odd = 0
for x in t:
    if x % 2 == 0:
        even +=1
    else:
        odd +=1

print("偶数个数:", even)
print("奇数个数:", odd)

row=int(input())
col=int(input())
for i in range(1,row+1):
    for j in range(1,col+1):
        print(i*j,end=" ")
    print()

for i in range(1,6):
    print("* "*i)
for i in range(4,0,-1):
    print("* "*i)
