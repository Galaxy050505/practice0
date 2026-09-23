name_list=['TOM','Lily','ROSE']
name_list.append('小名')
name_list.append([11,22])
name_list.extend('xiaoming')
name_list.extend(['小名','小紅'])
name_list.insert(3,'AAA')
#del name_list
del name_list[2]
del_name=name_list.pop(2)
print(del_name)
print(name_list)
