while True:
    try:
        a, b = [int(value) for value in input().split()]
        print(a ^ b)
    except EOFError:
        exit()