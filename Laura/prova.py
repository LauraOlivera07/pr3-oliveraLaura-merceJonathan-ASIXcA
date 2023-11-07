factura= float(input("Introdueix l'import de la teva factura (IVA inclós): "))
tclient = input("Tens la tarjeta client? (s/n): ").lower()

if tclient=="n":
    print(f"{factura:.2f}€")

else:
    if factura>=100:
        factura= factura*0.79 #precio sin iva
        pIva= factura*1.21
        print(f"{pIva:.2f}€")
    else:
        print(f"{factura:.2f}€")
