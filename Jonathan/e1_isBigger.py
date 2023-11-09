"""
Jonathan Merce
06/10/2023
ASIXc M03 UF1 A3
Descripció: Demana dos números, si el primer és més gran o igual que el segon els intercanvia. Mostra els valors per pantalla
"""

num1 = input("Quin és el primer número?")
num2 = input("Quin és el segon número?")

if num1 >= num2:
    print(num1, num2)

else: print(num2, num1)