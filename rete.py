''' 
Esercizio con grafico - Nodi 

Un matrice di nodi i * j 

Nodo 0 adiacente a 1 ma non a 2 e 3
Nodo 1 adiacente a 0, 2 e 3
Nodo 2 adiacente a 1 e 3 ma non a 0
Nodo 3 adiacente a 1 e 2 ma non a 0 
[{0, 1, 0, 0},
 {1, 0, 1, 1},
 {0, 1, 0, 1},
 {0, 1, 1, 0},
]

Il tuo compito è determinare se due nodi sono adiacenti in un grafo non orientato quando viene data la matrice di adiacenza e i due nodi.

TIPS: Ho provato a generare la rete attraverso dei semplici cicli for e il modulo random sfruttando il metodo randint().
      - Aggiornamenti futuri :
            - Costruire la rete in maniera più corretta, ovvero, se il nodo 1 è collegato al nodo 2, il nodo 2 nella sua riga non 
              può avere come valore in indice 1 lo zero.
'''
import random
from collections import defaultdict

class Rete():
    def __init__(self, nodi):
        self.nodi = nodi

    def creazione_grafico(self):
        dict_of_list = defaultdict(list)
        for i in range(self.nodi):
            for j in range(self.nodi):
                if i == j:
                    dict_of_list[i].append(0)
                else:
                    n = random.randint(0, 1)
                    dict_of_list[i].append(n)

        return dict_of_list



def controlla_maglia(maglia, num1, num2):
    if maglia.get(num1)[num2] == 1:
        print(maglia.get(num1))
        print(maglia.get(num1)[num2])
        return True
    else:
        return False
                    



nodi_totali = 1000 #int(input("Quanti nodi ha la tua rete ? "))
rete1 = Rete(nodi_totali)
maglia = rete1.creazione_grafico()
#print(maglia)
print(controlla_maglia(maglia, 270, 35))

