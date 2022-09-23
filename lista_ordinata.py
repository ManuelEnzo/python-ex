''' 
  Verificare se una lista è ordinata in maniera crescente. Se lista è vuota è ordinata.
 '''
 
 def isSorted(lista):
  l = len(lista)
  for i in range(0, l-1):
    if lista[i] > lista[i+1]:
      return False
  return True
 
  
lista = [2, 3, 4, 1, 10, 100]
x = isSorted(lista)

if x == True:
  print('Lista ordinata')
else:
  print('Lista NON ordinata')
