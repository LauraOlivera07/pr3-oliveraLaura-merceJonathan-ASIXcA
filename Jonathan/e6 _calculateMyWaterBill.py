"""
Jonathan Merce
06/10/2023
ASIXc M03 UF1 A3
Descripció: L'usuari introdueix la lletra del tipus d'habitatge i número de m3
d'aigua gastats. Mostrar per pantalla el preu total de la factura de l’aigua, arrodonit a 2 decimals
"""


# Tarifes per metre cúbic segons el tram
tarifes = {
    "1": 0.5849,
    "2": 1.1699,
    "3": 1.7548,
    "4": 2.3397,
    "5": 2.9246
}

# Quota mensual segons el tipus d'habitatge
quota_mensual = {
    'A': 2.46,
    'B': 6.4,
    'C': 7.25,
    'D': 11.21,
    'E': 12.10,
    'F': 17.28,
    'G': 28.01,
    'H': 40.50,
    'I': 61.31
}

# Demanar dades d'entrada a l'usuari
tipus_habitatge = input("Introdueix la lletra del tipus d'habitatge (A-I): ").upper()
consum_aigua = float(input("Introdueix el número de m³ d'aigua gastats: "))

# Calcula el preu total en funció del tram
if consum_aigua <= 6:
    preu_total = consum_aigua * tarifes[0]
elif 7 <= consum_aigua <= 9:
    preu_total = 6 * tarifes[0] + (consum_aigua - 6) * tarifes[1]
elif 10 <= consum_aigua <= 15:
    preu_total = 6 * tarifes[0] + 3 * tarifes[1] + (consum_aigua - 9) * tarifes[2]
elif 16 <= consum_aigua <= 18:
    preu_total = 6 * tarifes[0] + 3 * tarifes[1] + 6 * tarifes[2] + (consum_aigua - 15) * tarifes[3]
else:
    preu_total = 6 * tarifes[0] + 3 * tarifes[1] + 6 * tarifes[2] + 3 * tarifes[3] + (consum_aigua - 18) * tarifes[4]

# Afegeix la quota mensual segons l'habitatge
preu_total = preu_total + quota_mensual[tipus_habitatge]

# Mostra el resultat amb 2 decimals
print(f"El preu total de la factura de l'aigua és: {preu_total:.2f} €")
