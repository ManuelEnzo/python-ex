def somma_n():
    somma = 0
    
    while True:
        n = (int(input('inserisci numero da sommare: ')))
        if n == 0:
            break
        else:
            somma += n
            
    return(somma)

print(somma_n())
