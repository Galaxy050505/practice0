dict1={'name':'TOM','age':25,'gender':'male'}
print(dict1)
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)
for item in dict1.items():
    print(item)
for key,value in dict1.items():
    print(f'{key}={value}')