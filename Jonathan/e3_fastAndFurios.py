"""
Jonathan Merce
06/10/2023
ASIXc M03 UF1 A3
Descripció: Volem un programa que calculi la velocitat instantània i la velocitat mitjana.
"""

v_i = int(input("Quina és la velocitat inicial?"))
a = int(input("Quina és l'acceleracció?"))
t = int(input("Durant quant de temps?"))

v_inst = v_i + a * t
#print(v_inst)

if v_inst <= 0:
    print("parat, no es pot calcular la velocitat mitjana")

else:
    v_m = (v_i + v_inst) / 2
    print(f" La velocitat instantània és: {v_inst} i la velocitat mitjana és {v_m}")


"""
velocitat instantània = velocitat inicial + acceleració * temps
velocitat mitjana = (velocitat inicial + velocitat instantània )/2
"""
