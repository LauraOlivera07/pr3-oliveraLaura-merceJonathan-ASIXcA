"""
Laura Olivera Muñoz
Jonathan Mercè
9/11/2023
ASIXcA M03 UF1 A3
Descripció: Programa que detecta si tres números demanats han estat introduïts en ordre creixent.
"""
#demanem els 3 números en un mateix input

numeros= input("Introdueix 3 números: ").split()
numero1= int(numeros[0])
numero2= int(numeros[1])
numero3= int(numeros[2])

#S'avalua si el segon es més gran que el primer, o si el tercer és més gran que el segon
if numero2<=numero1 or numero3<=numero2:
        print("Els números no estàn en ordre creixent")
else:
        print("Els números estàn en ordre creixent")
