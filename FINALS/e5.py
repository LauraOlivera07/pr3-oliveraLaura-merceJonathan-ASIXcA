"""
Laura Olivera - Jonathan Merce
4/12/2023
ASIXcA M03 UF1 A4

Programa que realitza la multiplicació, de dos nombres sencers, mitjançant sumes
"""
try:
    num1, num2= [int(x) for x in input().split()]
    contador=0

    # si algun numero és negatiu el comptador restarà
    if num1<0:
        for i in range(num1, 0):
            contador -=num2
    elif num2<0:
        for i in range(num2, 0):
            contador -=num1
    elif num1<0 and num2<0:
        for i in range(num1, 0):
            contador += num2
    else:
        for i in range(1, num1+1):
            contador +=num2 #per cada iteració de l'1 al primer número+1, es sumarà el valor del segon número al comptador.

    print(contador)

except ValueError:
    print("Has d'introduïr 2 nombres sencers")