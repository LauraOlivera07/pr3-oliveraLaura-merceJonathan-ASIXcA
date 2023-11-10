"""
Laura Olivera Muñoz
Jonathan Mercè
10/11/2023
ASIXcA M03 UF1 A3
Descripció: Programa que demana dos números si el primer és més gran o igual que el segon els intercanvia.
I torna a mostrar els valors per pantalla
"""
numero1= int(input("Introdueix el primer número: "))
numero2= int(input("Introdueix el segon número: "))

#Cálculs per intercanviar el valor de dos variables
if numero1>=numero2:
    numero1= numero1+numero2
    numero2= numero1-numero2
    numero1= numero1-numero2

print(numero1, numero2)

