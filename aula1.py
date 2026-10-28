nome=input("Digite seu nome: ")
idade=input("Digite sua idade: ")
if nome and idade:
    print(f"Seu Nome é: {nome}")
    print(f"Seu Nome Invertido é: {nome[::-1]}")
    if " " in nome:
        print("Seu Nome contém espaços")
    else:
        print("Seu Nome não contém espaços")    
    print(f"Seu nome contém {len(nome)} letras")
    print(f"A primeira Letra do seu nome é: {nome[0]}")
    print(f"A ultima Letra do seu nome é: {nome[-1]}")
else:
    print("Você deixou campos vazios")