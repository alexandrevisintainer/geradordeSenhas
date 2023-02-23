chave = input("Digite a base da sua senha: ")
senha = ""

for letra in chave:
    if letra in "Aa": senha = senha + "1"
    elif letra in "Bb": senha = senha + "@"
    elif letra in "Cc": senha = senha + "2"
    elif letra in "Dd": senha = senha + "3"
    elif letra in "Ee": senha = senha + "4"
    elif letra in "Ff": senha = senha + "!"
    elif letra in "Gg": senha = senha + "@"
    elif letra in "Hh": senha = senha + "#"
    else: senha = senha + letra
print(senha)