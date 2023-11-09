"""
Laura Olivera Muñoz
Jonathan Mercè
9/11/2023
ASIXcA M03 UF1 A3
Descripció: Programa que comprovi si una data és correcte.
El programa ha de demanar una data, dia, mes i any (en el format DD/MM/AAAA).
Cal recordar que hi ha anys de traspàs. NO es pot fer servir funcions de calendari com ara datetime de Python.
"""
data= input("Introdueix una data (DD/MM/AAAA): ").split("/")
dia=int(data[0])
mes=int(data[1])
any=int(data[2])

#Hem de limitar el domini dels dies, mesos i anys
if 1>dia or dia>31 or mes>12 or mes<1 or any<=0:
    print("Data incorrecta")

#En aquests mesos només tenim 30 dies, si té més de 30 serà incorrecte
elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
        print("Data incorrecta")

#Febrer només pot tenir com a molt 29 dies
#Definim els casos en els quals pot tenir 29 dies i desprès limitem a 28 dies, que és el més comú
elif mes==2:
    if ((any%4==0) and (any%100!=0 or any%400==0) and dia==29) or 28>=dia:
        print("Data correcta")
    else:
        print("Data incorrecta")

else:
    print("Data correcta")

