quant = int(input())
weight = [2, 3, 5]

for i in range(quant):
    values = [float(i) for i in input().split()]
    weightedValues = [i * weight[idx] for idx, i in enumerate(values)]
    average = round(sum(weightedValues) / sum(weight), 1)
    print(average)
