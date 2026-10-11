a=float(input())

if a>=0 and a<=400:
    new=a*1.15
    b=new-a
    print(f'Novo salario: {new:.2f}')
    print(f'Reajuste ganho: {b:.2f}')
    print(f'Em percentual: 15 %')
elif a>400 and a<=800:
    new=a*1.12
    b=new-a
    print(f'Novo salario: {new:.2f}')
    print(f'Reajuste ganho: {b:.2f}')
    print(f'Em percentual: 12 %')
elif a>800 and a<=1200:
    new=a*1.10
    b=new-a
    print(f'Novo salario: {new:.2f}')
    print(f'Reajuste ganho: {b:.2f}')
    print(f'Em percentual: 10 %')
elif a>1200 and a<=2000:
    new=a*1.07
    b=new-a
    print(f'Novo salario: {new:.2f}')
    print(f'Reajuste ganho: {b:.2f}')
    print(f'Em percentual: 7 %')
elif a>2000:
    new=a*1.04
    b=new-a
    print(f'Novo salario: {new:.2f}')
    print(f'Reajuste ganho: {b:.2f}')
    print(f'Em percentual: 4 %')
