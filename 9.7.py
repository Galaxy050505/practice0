#綜合測試，8人隨機分配至3間辦公室
import random

teachers=['A','B','C','D','E','F','G','H']
offices=[[],[],[]]
for name in teachers:
    num=random.randint(0,2)
    offices[num].append(name)
print(offices)
i=1
for office in offices:
    print(f'辦公室{i}的人數是{len(office)},老師分別是{office}')
    for name in office:
        print(name)
#for 變數 in 資料
    i+=1