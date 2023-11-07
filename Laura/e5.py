"""
Programa que comprovi si una data és correcte.
El programa ha de demanar una data, dia, mes i any (en el format DD/MM/AAAA).
Cal recordar que hi ha anys de traspàs
"""
data= input("Introdueix una data (DD/MM/AAAA): ").split("/")
dia=data[0]
mes=data[1]
any=data[2]

print(any)