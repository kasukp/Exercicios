dias = int(input())

anos = int(dias / 365)
dias = dias % 365

meses = int(dias / 30)
dias = dias % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos, meses, dias))