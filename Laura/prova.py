data= input("Introdueix una data (DD/MM/AAAA): ").split("/")
dia=int(data[0])
mes=int(data[1])
any=int(data[2])

if mes>12 or dia>31 or any<0:
    print("Data incorrecta")

elif mes==4 or mes==6 or mes==9 or mes==11:
    if dia>30:
        print("Data incorrecta")

elif mes==2:
    if any%100==0 and any%400!=0 and dia>=29 or dia>=30:
        print("Data incorrecta")
else:
    print("Data correcta")
