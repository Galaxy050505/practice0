# 1. 读取四行输入，转换为浮点数
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

# 2. 计算加权平均数，权重为 2, 3, 4, 1，总和为 10
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10.0

# 3. 按照题目要求输出初始平均分（保留一位小数）
print(f"Media: {media:.1f}")

# 4. 根据条件进行判断
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:  # 隐含条件：5.0 <= media < 7.0
    print("Aluno em exame.")

    # 读取补考分数
    exam_score = float(input())
    print(f"Nota do exame: {exam_score:.1f}")

    # 计算最终平均分 = (原平均分 + 补考分) / 2
    final_media = (media + exam_score) / 2.0

    # 根据最终平均分再次判断
    if final_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    # 输出最终的平均分（注意这一步在条件判断之后，无论是否通过都要输出）
    print(f"Media final: {final_media:.1f}")