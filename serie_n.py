"""
    Scrivete un programma che acquisisca in input una serie di numeri terminata con invio e calcolate somma e media 
    dei numeri.

""" 

def serie_n():
    i = 0
    somma = 0
    media = 0
    while True:
        x = input('Inserisci numero : ' )
        if x ==  '':
            break
        else:
            i += 1
            somma += int(x)
    media = somma / i
    print('La somma è:', somma)
    print('La media è:', media)

serie_n()
    
