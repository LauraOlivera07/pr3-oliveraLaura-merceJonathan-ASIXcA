"""
Laura Olivera - Jonathan Merce
4/12/2023
ASIXcA M03 UF1 A4

Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""
try:
    alçada= int(input("Alçada del triangle (número entre 2 i 9): "))
    espai= " "
    contador= 0

    while alçada<2 or alçada>9:  #si l'alçada és inferior a 2 o superior a 9, torna a demanar-la
        alçada = int(input("L'alçada ha de ser entre 2 i 9. Introdueix un número vàlid: "))

    for i in range(1, alçada + 1):  # per cada iteració entre l'1 i l'alçada, depenent del valor de "i", imprimirà
        if i==1:                    # per pantalla una cosa diferent.
            contador +=1
            print(i)
        elif i==alçada:
            for i in range(1, alçada + 1):
                print(alçada, end=" ")  # per cada iteraciò entre l'1 i l'alçada imprimeix el valor de l'alçada i deixa un espai.
        else:
            print(f"{i}{espai*contador}{i}")
            contador +=2

except ValueError:
    print("Ha de ser un número sencer.")
