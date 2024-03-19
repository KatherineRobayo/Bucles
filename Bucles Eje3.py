'''Pedir al usuario que ingrese 2 números, después, se debe mostrar el rango de 
esos 2 números, pero, solo imprimiendo los números que sean impares. '''


numero1 = int(input("Introduzca el primer número: "))
numero2 = int(input("Introduzca el segundo número: "))


if numero1 < numero2:
    rango = range(numero1 + 1, numero2)
else:
    rango = range(numero2 + 1, numero1)

for numero in rango:
    print(numero, end=" ")

print()

