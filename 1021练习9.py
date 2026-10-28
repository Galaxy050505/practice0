while True:
    N = int(input())
    if N==0:
        break
    for i in range(N):
        row=[]
        for j in range(N):
            val=abs(i-j)+1
            row.append(str(val))
        print(' '.join(row))
    print()
