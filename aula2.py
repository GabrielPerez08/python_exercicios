numero=input("Digite um número")

try:
    numero_int = int(numero)
    par_impar="par" if numero_int % 2 == 0 else "ímpar"
    print(f"O número {numero_int} é {par_impar}")
except:
    print("Você não digitou um número inteiro.")