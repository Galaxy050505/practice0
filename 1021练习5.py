T=int(input())

for i in range(T):
    N=int(input())
    a=0
    b=1
    if N==0:
        print(f'Fib({N}) = 0')
    elif N==1:
        print(f'Fib({N}) = 1')
    else:
        for _ in range(1,N):
            a,b=b,a+b
        print(f'Fib({N}) = {b}')

