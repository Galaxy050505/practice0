#6/3遞歸
def return_num():
    return 100

result=return_num()
print(result)

def sum_number(num):
    if num==1:
        return 1
        return num+sum_number(num-1)
    return num+sum_number(num-1)

result=sum_number(3)
print(result)