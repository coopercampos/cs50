# Pelo algoritmo de Luhn, primeiro é preciso checar se o cartão de credito é válido através
# de uma checagem matemática
def check_luhn():
    number = input("Number: ")
    try:
        digitos = [int(n) for n in number]
    except ValueError:
        print("This program accepts only integers.")
        check_luhn()
    else:
        # Digitos que não vão ser multiplicados por dois no algoritmo de Luhn
        n1_dig = [digitos[i] for i in range(len(digitos)-1, -1, -2)]
        # Números multiplicados por dois
        n2_dig = [digitos[i]*2 for i in range(len(digitos)-2, -1, -2)]
        tt = "".join([str(n) for n in n2_dig])
        lista_n2 = [int(item) for item in tt]
        soma = sum(lista_n2)
        soma_final = soma + sum(n1_dig)

        if soma_final % 10 != 0:
            print("INVALID")
            return
        # checar bandeira
        first_two = f"{digitos[0]}{digitos[1]}"
        mastercard = ["51", "52", "53", "54", "55"]
        american = ["34", "37"]
        if digitos[0] == 4 and len(digitos) in range(13, 17):
            print("VISA")
        elif first_two in american and len(digitos) == 15:
            print("AMERICAN EXPRESS")
        elif first_two in mastercard and len(digitos) == 16:
            print("MASTERCARD")
        else:
            print("INVALID")
            return

check_luhn()