def main():
    n=int(input())
    for i in range(n):
        x,y=list(map(int,input().split()))
        if x>y:
            x,y=y,x
        sum_new=0
        for j in range(x+1,y):
            if j%2==1:
                sum_new+=j
        print(sum_new)
if __name__=='__main__':
    main()
