"""
  Realizzare il wrapping dei bit verso sinistra di una cifra. 
"""

def wrapping(stringa):
    x = len(stringa)-1
    stringa_n = ''
    for i in range (x):
        stringa_n += stringa[i]
     
    stringa_n = stringa[x] + stringa_n
    
    return stringa_n
    
print('Stringa finale:', wrapping('001001'))
