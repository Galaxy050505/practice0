#continue
i=1
while i<=5:
    if i==2:
        print(f'吃第{i}個蘋果時那顆壞掉了')
        #若使用continue在之前要修改計數器，否則進入死循環
        i+=1
        continue
    print(f'吃第{i}個蘋果，還沒吃飽繼續吃')
    i+=1