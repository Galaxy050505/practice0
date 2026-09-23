#5/29函數
#因為函數要先定義才能調用，故步驟2和3要寫在1之上
def sel_func():
    print('查詢存款')
    print('存款')
    print('取款')
#1.搭建框架
print('登入成功')
sel_func()
#2.確定功能介面
x=10000
print('您的餘額是10000')
sel_func()
y=int(input('取出多少錢?'))
print(f'餘額為{x-y}元')
sel_func()
#3.封裝函數
#4.調用函數