#Programa que demana dos números si el primer és més gran o igual que el segon els intercanvia.
# I torna a mostrar els valors per pantalla

numero1= int(input("Introdueix el primer número: "))
numero2= int(input("Introdueix el segon número: "))

if numero1>=numero2:
    numero1= numero1+numero2
    numero2= numero1-numero2
    numero1= numero1-numero2

print(numero1, numero2)

