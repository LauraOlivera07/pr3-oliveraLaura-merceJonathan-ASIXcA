"""
Laura Olivera Muñoz
Jonathan Mercè
10/11/2023
ASIXcA M03 UF1 A3
Descripció: Programa que demana l'import d'una factura, amb iva inclòs.
Calcula l'import amb descompte, en cas de tenir la targeta de client, tenint en compte els següents criteris:
Si l'import de la factura, és igual o superior a 100 €, se li aplica un descompte del 21%, en cas contrari no se li aplica cap descompte.
El descompte es calcula al preu final, i no a la “base imponible”. I després si li aplica l’IVA. Precio total = Base imponible * Tipo de IVA
"""
factura= float(input("Introdueix l'import de la teva factura (IVA inclós): "))
tclient = input("Tens la tarjeta client? (s/n): ").lower()

#S'han de complir aquestes dues condicions per poder aplicar el descompte
if factura>=100 and tclient=="s":
        pdescuento= factura*0.79  #Cálcul per aplicar el descompte de 21% a la factura introduïda
        pfinal= pdescuento*1.21  #multipliquem per 1.21 per aplicar l'IVA al preu amb descompte
        print(f"{pfinal:.2f}€")
else:
    print(f"{factura:.2f}€")

