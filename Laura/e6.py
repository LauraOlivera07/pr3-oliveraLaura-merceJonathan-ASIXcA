"""
Laura Olivera Muñoz
Jonathan Mercè
9/11/2023
ASIXcA M03 UF1 A3
Descripció: L'usuari introdueix la lletra del tipus d'habitatge i número de m3 d'aigua gastats. Mostrar per pantalla el preu total de la factura de l’aigua.
Arrodonit a 2 decimals
"""

habitatge= input().upper()
aigua= float(input())
qfixa= 0
tram= 0
preutram=0

#Asignarem un valor diferent a la quota fixa mensual depenent del tipus d'habitatge
match habitatge:
    case "A": qfixa=2.46
    case "B": qfixa=6.40
    case "C": qfixa=7.25
    case "D": qfixa=11.21
    case "E": qfixa=12.10
    case "F": qfixa=17.28
    case "G": qfixa=28.01
    case "H": qfixa=40.50
    case "I": qfixa=61.31

#Asignarem un tram diferent depenent del número de m3 d'aigua gastats
if 0<=aigua<=6:
    tram= 1
elif 7<=aigua<=9:
    tram= 2
elif 10<=aigua<=15:
    tram= 3
elif 16<=aigua<=18:
    tram= 4
elif 18<aigua:
    tram= 5

#el preu per m3 d'aigua gastats varia depenent del tram
match tram:
    case 1: preutram=0.5849
    case 2: preutram=1.1699
    case 3: preutram=1.7548
    case 4: preutram=2.3397
    case 5: preutram=2.9246

#Calculem el preu final i al mateix temps arrodonim a 2 decimals
preu= round(aigua*preutram+qfixa, 2)

print(f"El preu total de la teva factura és de {preu}€")
