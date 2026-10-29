entrada=input("Digite seu primeiro nome: ")
nome=len(entrada)

try:
    if nome >=1 and nome <= 4:
        print("Seu nome é curto")
    elif nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é longo")
except:
    print("Você não digitou um nome válido.")