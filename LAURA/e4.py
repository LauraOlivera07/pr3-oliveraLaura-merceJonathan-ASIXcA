"""
Laura Olivera - Jonathan Merce
4/12/2023
ASIXcA M03 UF1 A4

Programa que imprimeix un tauler d’escacs per pantalla. Un taulell d’escacs comença
amb la casella  Blanca i és de mida 8x8 sempre ;-)
"""
for i in range(8, 0, -1): #per cada iteració del 8 al 0
   print(i, end=" ") #imprimeix el número, que es el valor de "i"
   if i%2==0: #si el número de la iteració és parell
      for j in range (1, 5): #per cada iteració entre 1 i 5 imprimirà el següent
         print("██   ", end="")
   else: #si el número de la iteració no és parell
      for x in range (1, 5):#per cada iteració entre 1 i 5 imprimirà el següent
         print("   ██", end="")
   print()

for i in range(97, 105): #imprimeix les lletres
   print(f" {chr(i)} ", end="")
