for i in range(int(input())):
    num = int(input())

    if num == 0:
        print("NULL")
        continue
    elif num % 2 == 0:
        print("EVEN", end=" ")
    else: 
        print("ODD", end=" ")
    
    if num < 0:
        print("NEGATIVE")
    else:
        print("POSITIVE")