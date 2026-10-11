a,b,c=map(float,input().split())
Perimetro=a+b+c
Area=(a+b)*c/2
if a+b>c and a+c>b and b+c>a:
    print(f'Perimetro = {Perimetro:.1f}')
else:
    print(f'Area = {Area:.1f}')

