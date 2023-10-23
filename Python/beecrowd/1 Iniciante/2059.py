game = [int(i) for i in input().split()]

def win(i):
    print(f"Jogador {i} ganha!")

if game[3] != game[4]:
    win(1)
elif game[4] == game[3] == 1:
    win(2)
elif (game[1] + game[2]) % 2 == game[0]:
    win(2)
else:
    win(1)