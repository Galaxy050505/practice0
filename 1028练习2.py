"""while True:
    try:
        line = input().strip()
        if not line:
            break
        str_main,substr = line.split()

        max_str=str_main[0]
        max_index=0

        for i in range (len(str_main)):
            if str_main[i]>max_str:
                max_index=i
        result_str=str_main[:max_index+1]+substr+str_main[max_index+1:]
        print(result_str)
    except EOFError:
        break
"""
while True:
    try:
        line = input().strip()
        if not line:
            break

        str_main, substr = line.split()

        # 初始化最大字符为第一个字符，索引为 0
        max_char = str_main[0]
        max_idx = 0

        # 遍历寻找最大字符
        for i in range(len(str_main)):
            # 注意：这里用 > 而不是 >=，保证了如果有多个最大字符，只记录第一个
            if str_main[i] > max_char:
                max_char = str_main[i]
                max_idx = i

        # 拼接
        result = str_main[:max_idx + 1] + substr + str_main[max_idx + 1:]
        print(result)

    except EOFError:
        break