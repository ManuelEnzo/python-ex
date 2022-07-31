
PAGA_STR = 1.5

def calcolo_paga(paga, ore):
    #print('Test 1 Passed')

    x = input('Ha fatto anche straordinari: (y/n)')
    if x == 'y':
        ore_str = float(input('Quante ore ?: '))
        paga_straordinaria = (paga * PAGA_STR) * ore_str
        return int(paga * ore + paga_straordinaria)
    else:
        return int(paga * ore)





def lavoratore():
    paga_oraria = float(input('Paga Oraria: '))
    numero_ore = float(input('Ore lavorate: '))
    
    print(calcolo_paga(paga_oraria, numero_ore), '€')


lavoratore()
