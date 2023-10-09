scores = [float(i) for i in input().split()]
weight = [2, 3, 4, 1]

weightedScore = [i * weight[idx] for idx, i in enumerate(scores)]
average = round(sum(weightedScore) / sum(weight), 1)
print(f"Media: {average}")

if average < 5:
    print("Aluno reprovado.")
    exit()
elif average >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")
    examScore = float(input())
    print(f"Nota do exame: {examScore}")
    
    average = round((average + examScore) / 2, 1)
    if average < 5:
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")
    print(f"Media final: {average}")