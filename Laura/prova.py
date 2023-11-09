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

#Definim els casos en els que seria incorrecte que hi hagi 29 dies (com a molt 28)
#Aquest més mai pot tenir més de 29 dies
elif mes==2 and (((any%4!=0) or (any%100==0 and any%400!=0) and dia>28) or dia>29):
        print("Data incorrecta")
else:
    print("Data correcta")
