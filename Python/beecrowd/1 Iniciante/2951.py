quantRunes, minFriendship = [int(i) for i in input().split()]
runes = {i: int(j) for k in range(quantRunes) for i, j in [input().split()]}

input() # valor desnecessário

total = sum(runes[i] for i in input().split())
print(total)

if total >= minFriendship:
    print("You shall pass!")
else:
    print("My precioooous")