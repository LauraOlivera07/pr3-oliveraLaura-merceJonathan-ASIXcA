"""
Laura Olivera - Jonathan Merce
4/12/2023
ASIXcA M03 UF1 A4

Programa que mostra per pantalla la suma de tots els nombres senars i de tots els nombres
parells inferiors a un número límit, que l’usuari introdueix per teclat.
"""

try:
    limit= int(input("Número límit: "))
    parells= 0
    senars=0

    while limit<0: #per impedir un imput negatiu
        print("No pot ser un nombre negatiu.")
        limit= int(input("Número limit: "))

    for i in range(1, limit): #per cada iteració entre l'1 i el límit
        if i%2==0:
            parells=parells+i #si el valor de "i" és parell, sumarà el valor de "i" al comptador de nombres parells.
        else:
            senars=senars+i #si el valor de "i" no és parell, sumarà el valor de "i" al comptador de nombres senars.

    print(f"La suma dels números senars és {senars} i la suma dels parells és {parells}.")

except ValueError:
    print("Has d'introduïr un nombre sencer.")

