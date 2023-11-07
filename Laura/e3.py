"""
Volem un programa que calculi la velocitat instantània i la velocitat mitjana. Cal demanar velocitat inicial (m/s), l'acceleració (m/s2) i el temps. Si la velocitat instantània és inferior o igual a 0, has d'indicar que està parat i no pots calcular la velocitat mitjana.
velocitat instantània = velocitat inicial + acceleració * temps
velocitat mitjana = (velocitat inicial + velocitat instantània )/2

"""

vInicial= float(input("Introdueix la velocitat inicial (m/s): "))
xlr8= float(input("Introdueix l'acceleració (m/s²): "))
temps= float(input("Introdueix el temps (segons): "))

vinst= vInicial+xlr8*temps

if vinst<=0:
        print("Està parat. No es pot calcular la velocitat mitjana")
else:
    vmitj= (vInicial+vinst)/2
    print(f"La velocitat instantànea és de {vinst:.2f} m/s, i la velocitat mitjana és de {vmitj:.2f} m/s²")

