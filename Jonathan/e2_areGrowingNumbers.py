"""
Jonathan Merce
06/10/2023
ASIXc M03 UF1 A3
Descripció: Programa que detecta si tres números demanats han estat introduïts en ordre creixent.
"""
#Demana a l'usuari tres números
num1 = int(input("Quin és el primer número?"))
num2 = int(input("Quin és el segon número?"))
num3 = int(input("Quin és el tercer número?"))

#Compara els números entre si
if num1 >= num2 >= num3:
        print(f"Els números ordenats de major a menor són: {num1}, {num2}, {num3}")
elif num1 >= num3 >= num2:
        print(f"Els números ordenats de major a menor són: {num1}, {num3}, {num2}")
elif num2 >= num1 >= num3:
        print(f"Els números ordenats de major a menor són: {num2}, {num1}, {num3}")
elif num2 >= num3 >= num1:
        print(f"Els números ordenats de major a menor són: {num2}, {num3}, {num1}")
elif num3 >= num1 >= num2:
        print(f"Els números ordenats de major a menor són: {num3}, {num1}, {num2}")
else:
        print(f"Els números ordenats de major a menor són: {num2}, {num1}, {num3}")






