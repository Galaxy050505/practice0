def main():
    try:
        n=int(input().strip())
    except EOFError:
        return
    count_c=0
    count_r=0
    count_f=0
    for i in range(n):
        line=input().strip().split()
        if not line:
            continue
        num=int(line[0])
        animal_type=line[1]
        if animal_type=='C':
            count_c+=num
        elif animal_type=='R':
            count_r+=num
        elif animal_type=='F':
            count_f+=num
    total=count_c+count_r+count_f
    if total>0:
        c_c=(count_c/total)*100
        c_r=(count_r/total)*100
        c_f=(count_f/total)*100
    else:
        c_c=0
        c_r=0
        c_f=0
    print(f'Total: {total} animals')
    print(f'Total coneys: {count_c}')
    print(f'Total rats: {count_r}')
    print(f'Total frogs: {count_f}')
    print(f'Percentage of coneys: {c_c:.2f} %')
    print(f'Percentage of rats: {c_r:.2f} %')
    print(f'Percentage of frogs: {c_f:.2f} %')
if __name__ == '__main__':
    main()
