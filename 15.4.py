def return_num():
    return 5,50

result = return_num()
print(result)
#返回值是元祖

def return_num():
    #return後可以直接書寫元祖、列表、字典，返回多個值
    return {'name':'Elieen'}#字典

result = return_num()
print(result)

def return_num():
    return [5,50]#列表

result = return_num()
print(result)