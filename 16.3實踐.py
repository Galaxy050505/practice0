def function_print():
    print('請選擇功能-----')
    print('1.添加學員')
    print('2.刪除學員')
    print('3.修改學員')
    print('4.查詢學員')
    print('5.顯示所有學員')
    print('6.退出系統')
    print('-'*10)
info=[]
#序號1，添加
def add_info():
    """添加學員函數"""
    new_name=input('請輸入名字:')
    new_id=input('請輸入編號')
    global info
    for i in info:
        if new_name==i['name'] or new_id==i['id']:
            print('名稱或編號重複')
            return

    info_dict={}
    info_dict['id']=new_id
    info_dict['name']=new_name
    info.append(info_dict)
    print(info)
#序號2，刪除
def del_info():
    """刪除函數"""
    del_name=input('請輸入要刪除的名字')
    global info
    for i in info:
        if del_name==i['name']:
            info.remove(i)
            print('成功刪除')
            break
#若是沒有break，要刪除'TOM'，會檢查完info中所有資料，並刪除所有'TOM'
#有break則是刪除第一個'TOM'並立刻離開for循環
    else:
        print('未找到要刪除的名字')
    print(info)
#序號3，修改
def modify_info():
    """修改函數"""
    name=input('請輸入要修改的原暱稱:')
    global info
    for i in info:
        if name==i['name']:
            new_name=input('請輸入新暱稱:')#只是拿到使用者給的資料
            #防止新暱稱與資料中暱稱重複
            for j in info:
                if new_name==j['name']:
                    print('暱稱重複，修改失敗')
                    return
            i['name']=new_name#讓資料改變
            print('修改成功')
            break

    else:
        print('該暱稱不存在')
    print(info)
#序號4，查詢
def search_info():
    """查詢學員"""
    search_name=input('請輸入要查找的學員名字')
    global info
    for i in info:
        if search_name==i['name']:
            print('查找到的信息如下')
            print(f"該學園的編號是{i['id']},名字是{i['name']}")
            break
    else:print('該學員不存在')
    print(info)
#序號5，顯示所有
def print_all():
    """顯示函數"""
    print('編號\t姓名')
    for i in info:
        print(f"{i['id']},{i['name']}")

#序號6，退出系統

#序號1至6總程式
while True:
    function_print()
    user_num=int(input('請輸入功能序號:'))

    if user_num==1:
        add_info()
    elif user_num==2:
        del_info()
    elif user_num==3:
        modify_info()
    elif user_num==4:
        search_info()
    elif user_num==5:
        print_all()
    elif user_num==6:
        exit_flag=input('確定要退出嗎?yes/no:')
        if exit_flag=='yes':
            break
    else:
        print('僅可輸入1至6')
