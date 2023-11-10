"""
Laura Olivera Muñoz
Jonathan Mercè
10/11/2023
ASIXcA M03 UF1 A3
Descripció: Volem un programa que calculi la velocitat instantània i la velocitat mitjana.
Cal demanar velocitat inicial (m/s), l'acceleració (m/s²) i el temps.
Si la velocitat instantània és inferior o igual a 0, has d'indicar que està parat i no pots calcular la velocitat mitjana.
"""

vInicial= float(input("Introdueix la velocitat inicial (m/s): "))
acceleracio= float(input("Introdueix l'acceleració (m/s²): "))
temps= float(input("Introdueix el temps (segons): "))

#Calculem la velocitat instantània
vinst= vInicial + acceleracio * temps

if vinst<=0: #Farem directament el print perquè no té sentit calcular la mitjana si ja sabem que està parat
        print("Està parat. No es pot calcular la velocitat mitjana")
else:
    vmitj= (vInicial+vinst)/2 #En aquest cas si calculem la velocitat mitjana
    print(f"La velocitat instantànea és de {vinst:.2f} m/s, i la velocitat mitjana és de {vmitj:.2f} m/s")

