

#definisco la funzione addizione
def addizione():
    #qua quello che deve eseguire la funzione
    risultato = a + b
    print("Il risultato dell'addizione è " + str(risultato))

#definisco la funzione sottrazione
def sottrazione():
    #qua quello che deve eseguire la funzione
   risultato = a-b
   print("Il risultato della sottrazione è " + str(risultato))

#definisco la funzione moltiplizazione
def moltiplicazione():
    #qua quello che deve eseguire la funzione
    risultato = a*b
    print("Il risultato dell'addizione è " + str(risultato))

#definisco la funzione divisione
def divisione():
    #qua quello che deve eseguire la funzione
    risultato = a / b
    print("Il risultato dell'addizione è " + str(risultato))

import time

print ("ciao benvenuto nella calcolatrie in due minuti")
print ("scegli un operazione")
print ("1) addizione")
print ("2) sottrazione")
print ("3) moltiplicazione")
print ("4) divisione")
print ("5) potenza")

operazione = input()

print("scegli due numeri")
time.sleep(1.5)
print("IL PRIMO NUMERO È?")
a=int(input())

time.sleep(1.5)

print("IL SECONDO NUMERO È?")
b=int(input())

if operazione == "1":
 addizione()
if operazione == "2":
 sottrazione()
if operazione == "3":
 moltiplicazione()
if operazione == "4":
 divisione()
if operazione == "5":
 risultato = pow(a,b)
 print ("il risultato della potenza è" + str(risultato)) 

print("press enter to exit")
time.sleep(1)
input()


