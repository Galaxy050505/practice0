a,b=map(int,input().split())
A=b+24-a
B=b-a
if 0<=a and b<=23 and a>b:
    print(f'O JOGO DUROU {A} HORA(S)')
elif 0<=a and b<=23 and a==b:
    print(f'O JOGO DUROU 24 HORA(S)')
elif 0<=a and b<=23 and a<b:

    print(f'O JOGO DUROU {B} HORA(S)')
