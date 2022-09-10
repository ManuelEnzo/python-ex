#Questo è uno dei semplici progetti Python. 
#Puoi anche chiamarlo un mini-gioco. 
#Questo progetto è particolarmente utile per i principianti. 
#Crea un programma in cui il computer sceglie casualmente un numero compreso tra 1 e 10, da 1 a 100 o qualsiasi intervallo. 
#Quindi dai agli utenti un suggerimento per indovinare il numero. 
#Ogni volta che l'utente sbaglia, ottiene un altro indizio e il suo punteggio viene ridotto. 
#L'indizio può essere divisibile, maggiore o minore o una combinazione di tutti.

import random 

START = 1
META = 25
END = 50
PUNTEGGIO = 10


def meta(n_p, n_u):
  if n_p > META :
    print('Il numero del pc è maggiore di 25 &')
  else :
    print('Il numero del pc è minore di 25 &')

def indizio(num_pc, num_utente, c):
  if c == 1:
    meta(num_pc, num_utente)
  if num_pc % num_utente == 0:
    print('Il numero del pc è divisibile per', num_utente)
  elif num_pc > num_utente :
    print('Il numero che hai inserito è troppo piccolo')
  elif num_pc < num_utente:
    print('Il numero che hai inserito è troppo grande')
    
def punteggio(p):
  if p == 0:
    print('Hai finito i tentativi!!')
  else:
    print('Il tuo punteggio è: ', p) 
  
def scelta_utente(num_pc, p):
  c = 0
  lista_numeri = []
  while True:
    num_utente = int(input('\nInserisci Numero da indovinare: (1-50) '))
    lista_numeri.append(num_utente)
    c += 1
    if num_utente == num_pc:
      punteggio(p)
      print('Bravo!, Sei riuscito a totalizzare ', p, 'punti')
      break
    else:
      p -= 1
      punteggio(p)
      indizio(num_pc, num_utente, c)
      print('\nNumeri inseriti fino ad ora: ', lista_numeri)


def scelta_computer(s, e, p):
  num_pc = random.randint(s, e)
  scelta_utente(num_pc, p)



scelta_computer(START, END, PUNTEGGIO)
