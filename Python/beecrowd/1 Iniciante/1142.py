num = 1

for i in range(int(input())):
    for j in range(4):
        if j == 3:
            print("PUM")
        else:
            print(num, end=" ")
        num += 1