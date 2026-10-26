dict0={'a':1,'b':2,'c':3,'d':4}
dict1={'a':1,'b':3,'c':5}
print(dict0)
print(dict1)
merged_dict=dict0|dict1
print(merged_dict)
remove=merged_dict.pop('b')
print(remove)