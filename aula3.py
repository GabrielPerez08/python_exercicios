horas=input("Digite que horas são em numero: ")
horas_int = int(horas)

try:
    if horas_int >=0 and horas_int <= 11:
        print("Bom dia")
    elif horas_int <= 17:
        print("Boa tarde")
    else:
        print("Boa noite")
except:
    print("Não conheço essa hora.")