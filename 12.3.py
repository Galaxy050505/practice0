counts={'A':268,'B':125,'C':201,'D':199,'E':23}
print(counts.items())
dict1={key:value for key,value in counts.items() if value>=200}
print(dict1)