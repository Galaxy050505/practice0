N=int(input())
for i in range(2,N+1):
    X=True
    for j in range(2,i):
        if i%j==0:
            X=False
            break
    if X:
        print(i)
