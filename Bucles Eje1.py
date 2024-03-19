'''Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero'''

numero = int(input("digite un numero del cual se generara una tabla de multiplicar"))

i = 0 
print(f" la tabla de multiplicar que se genera a partir del numero {numero} es: \n")

for i in range(1,10+1):
    resultado = i*numero
    
    print(f" {numero} x {i} = {resultado}")

