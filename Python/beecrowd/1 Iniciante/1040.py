scores = [float(i) for i in input().split()]
weight = [2, 3, 4, 1]

weighted_score = [i * weight[idx] for idx, i in enumerate(scores)]
average = round(sum(weighted_score) / sum(weight), 1)
print(f"Media: {average}")

if average < 5:
    print("Aluno reprovado.")
    exit()
elif average >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")
    exam_score = float(input())
    print(f"Nota do exame: {exam_score}")

    average = round((average + exam_score) / 2, 1)
    if average < 5:
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")
    print(f"Media final: {average}")