#猜拳
import random
player=int(input('請出拳,0=石頭、1=剪刀、2=布'))
computer=random.randint(0,2)
print(computer)
if ((player==0) and (computer==1)) or ((player==1) and (computer==2)) or ((player==2) and (computer==0)):
    print('玩家獲勝')
elif player==computer:
    print('平局，再來一局')
else:
    print('電腦獲勝')