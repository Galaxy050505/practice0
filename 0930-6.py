SS0=int(input())
MM=SS0//60
SS=SS0-MM*60
HH=MM//60
MM=MM%60
print(f'{HH}:{MM}:{SS}')
