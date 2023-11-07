"""
Programa que demana l'import d'una factura, amb iva inclòs.
Calcula l'import amb descompte, en cas de tenir la targeta de client,
tenint en compte els següents criteris:

Si l'import de la factura, és igual o superior a 100 €, se li aplica un descompte del 21%,
en cas contrari no se li aplica cap descompte.
El descompte es calcula al preu final,  i no a la “base imponible”. I després si li aplica l’IVA
Precio total = Base imponible * Tipo de IVA

"""
factura= float(input("Introdueix l'import de la teva factura (IVA inclós): "))
tclient = input("Tens la tarjeta client? (s/n): ").lower()

if factura>=100:
    if tclient=="s":
        factura= factura*0.79 #precio sin iva
        pIva= factura*1.21
        print(f"{pIva:.2f}€")
    else:
        print(f"{factura:.2f}€")
else:
    print(f"{factura:.2f}€")