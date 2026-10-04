INPUT = float(input())
centavos = int(round(INPUT * 100))#round四舍五入
notas=[10000,5000,2000,1000,500,200]
print('notas:')
for nota in notas:
    qtd = centavos // nota
    centavos %= nota   #   %为计算相除后余数
    print(f'{qtd} nota(s) de R$ {nota//100}.{nota%100:02d}')
moedas=[100,50,25,10,5,1]
print('moedas:')
for moeda in moedas:
    qtd = centavos // moeda
    centavos %= moeda
    print(f'{qtd} moeda(s) de R$ {moeda//100}.{moeda%100:02d}')
