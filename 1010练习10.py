"""a,b,c,d=map(int,input().split())
if c<a and d<b and 0<=a and c<=23 and 0<=b and d<=59:
    HOURS=c+24-a
    MINS=d+60-b
    print(f'O JOGO DUROU {HOURS} HORA(S) E {MINS} MINUTO(S)')
else:
    if c<a and d>b and 0<=a and c<=23 and 0<=b and d<=59:
        HOURS=c+24-a
        MINS=d-b
        print(f'O JOGO DUROU {HOURS} HORA(S) E {MINS} MINUTO(S)')
    else:
        if c>a and d<b and 0<=a and c<=23 and 0<=b and d<=59:
            HOURS=c-a
            MINS=d+60-b
            print(f'O JOGO DUROU {HOURS} HORA(S) E {MINS} MINUTO(S)')
        else:
            if c>a and d>b and 0<=a and c<=23 and 0<=b and d<=59:
                HOURS=c-a
                MINS=d-b
                print(f'O JOGO DUROU {HOURS} HORA(S) E {MINS} MINUTO(S)')
"""
a, b, c, d = map(int, input().split())

# 1. 将开始和结束时间统一换算成总分钟数
start = a * 60 + b
end = c * 60 + d

# 2. 如果结束时间 <= 开始时间，说明跨天了（加上24小时）
if end <= start:
    end += 24 * 60

# 3. 计算时间差
diff = end - start

# 4. 将总分钟数转换回 小时 和 分钟
h = diff // 60
m = diff % 60

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')