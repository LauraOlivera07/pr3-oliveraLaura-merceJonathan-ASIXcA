"""
Jonathan Merce
06/10/2023
ASIXc M03 UF1 A3
Descripció: Programa que demana l'import d'una factura, amb iva inclòs.
Calcula l'import amb descompte, en cas de tenir la targeta de client,
tenint en compte els següents criteris:

Si l'import de la factura, és igual o superior a 100 €, se li aplica un descompte del 21%,
en cas contrari no se li aplica cap descompte.
El descompte es calcula al preu final,  i no a la “base imponible”. I després si li aplica l’IVA
Preu total = Base imponible * Tipo de IVA
"""

IVA = 0.21

#Demanem l'import total de la factura
import_total = float(input("Introdueix l'import total de la teva factura (IVA inclós): "))

#Demanem si te targeta client
tclient = input("Tens la targeta client? (s/n): ").lower()

# Calculem la base imponible (l'import sense IVA)
base_imponible = import_total / (1 + IVA)

# Comprovem si l'import de la factura és igual o superior a 100 euros i si té la targeta de client
if base_imponible >= 100 and tclient == "s":
        base_imponible =  base_imponible * 0.79

# Calculem el preu final amb IVA
import_total = base_imponible * (1 + IVA)

print(f"L'import final de la factura després d'aplicar els descomptes i amb IVA és: {import_total:.2f}€")



