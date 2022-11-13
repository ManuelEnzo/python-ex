'''
Creazione di un semplice algoritmo di Crittografia che imposta il carattere in entrata al valore del carattere opposto dell'alfabeto.
Esempio:
  - Se il carattere è c allora il carattere in output sarà y.
  
Attenzione !
  - L'algoritmo fa distinzione se il carattere è:
    - maiuscolo;
    - minuscolo;
    - simbolo;
    - numero.
Liste di caratteri dell'alfabeto 
    PS: (possibile la realizzazione anche grazie all'utilizzo delle semplici stringhe)
    
    myAlpha = ['a','b','c','d','e','f','g','h','i','j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    myAlphaU = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    valid_symbols = "!@#$%^&*()_-+={}[]'."

'''

def atbash(txt):
    myAlpha = ['a','b','c','d','e','f','g','h','i','j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    myAlphaU = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    valid_symbols = "!@#$%^&*()_-+={}[]'."

    s = (len(myAlpha))
    new_string = ""

    for i in txt:
        if i.isalpha():
            if i.isupper():
                new_string = new_string + (myAlphaU[s - myAlphaU.index(i) - 1])
            else:
                new_string = new_string + (myAlpha[s - myAlpha.index(i) - 1])
        elif i in valid_symbols:
            new_string = new_string + i
        elif i == " ":
            new_string = new_string + " "
        elif i.isnumeric():
            new_string = new_string + i

    return new_string

print(atbash("Yvmevmfgr hfo nrl Yolt Xlwrmtoruv.yolt"))

#Benvenuti sul mio Blog Codinglife.blog
