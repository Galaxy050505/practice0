#while實現
list1=[]
i=0
while i<10:
    list1.append(i)
    i+=1
print(list1)
#for實現
list2=[]
for i in list2:
    list2.append(i)
print(list2)
#列表推導式實現
list3=[i for i in range(10)]
print(list3)
#結構:結果 for 變數 in 資料
list4=[i*i for i in range(5)]
print(list4)
#for + if 循環
list5=[]
for i in range(10):
    if i % 2 ==0:
        list5.append(i)
#改寫成列表推導式
list6=[i for i in range(10) if i%2==0]
print(list6)