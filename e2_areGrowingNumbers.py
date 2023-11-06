"""
Jonathan Merce
06/10/2023
ASIXc M03 UF1 A3
Descripció: Programa que detecta si tres números demanats han estat introduïts en ordre creixent.
"""

num1 = int(input("Quin és el primer número?"))
num2 = int(input("Quin és el segon número?"))
num3 = int(input("Quin és el tercer número?"))

if num1 >= num2 and num2 >= num3:
        print(f"{num1, num2, num3}")

elif num2 >= num1 and num1 >= num3:
        print(f"{num2, num1, num3}")

elif num3 >= num1 and num1 >= num2:
        print(f"{num2, num1, num3}")

# elif(num2 <= num1 <= num3:
