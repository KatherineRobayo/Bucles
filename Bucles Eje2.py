'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos 
los años que ha cumplido (desde 1 hasta su edad).'''

edad = int(input("¿Cuántos años tiene actualmente? "))


for i in range(1, edad+1 ):
  
  año = 2024 - i

  print(año)

''' NO SE MUESTRAS EL AÑO DE NACIMIENTO YA QUE SOLO SE MUESTRA DESDE EL AÑO QUE CUMPLIO 1 AÑO DE EDAD
'''