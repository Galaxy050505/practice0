#5/24
name_list=['TOM','Lily','ROSE']
print(name_list)
print(name_list[0])
print(name_list.index('TOM'))
print(name_list.count('Lily'))
print(len(name_list))
name=input('請輸入您的帳戶')
if name in name_list:
    print('用戶名字重複')
else:
    print('名字未重複,可註冊')
