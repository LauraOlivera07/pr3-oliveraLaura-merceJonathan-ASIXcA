#Programa que detecta si tres números demanats han estat introduïts en ordre creixent.

try:
    numeros= input("Introdueix 3 números: ")
    numero= numeros.split()
    numero1= int(numero[0])
    numero2= int(numero[1])
    numero3= int(numero[2])

    if numero2<=numero1 or numero3<=numero2:
        print("Els números no estàn en ordre creixent")
    else:
        print("Els números estàn en ordre creixent")

except ValueError:
    print("Has d'introduir un número vàlid")
