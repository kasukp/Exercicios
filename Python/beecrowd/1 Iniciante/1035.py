a, b, c, d = [int(i) for i in input().split()]


def selection_test():
    ## Inverso dos requisitos
    if not b > c:
        return 1
    if not d > a:
        return 1
    if not c + d > a + b:
        return 1
    if not (c > 0 and d > 0):
        return 1
    if a % 2 != 0:
        return 1
    return 0

if selection_test() != 0:
    print("Valores nao aceitos")
else:
    print("Valores aceitos")