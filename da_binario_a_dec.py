def converti(x):
    somma = 0
    esp = len(x) - 1  #Perchè - 1? Perche len conta 3 caratteri quindi esp = n_caratteri ma a me serve che gli esponenti vadano da 0 a n_caratteri quindi (n_caratteri-1)
    for i in x:
        somma = somma + (int(i) *( 2**esp) )
        esp -= 1
    print(somma)

def lettura_numero():
    x = input('Leggi numero binario (0-1): ')
    converti(x)


lettura_numero()