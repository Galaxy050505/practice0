N=int(input())
for i in range(1,N+1):
    count_j = 0
    for j in range(1,i):
        if i%j==0:
            count_j+=j
    if i==count_j and i!=1:
        print(i)
