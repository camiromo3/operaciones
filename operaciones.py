print("estes es un proyecto de operaciones matematicas")
nombre = input("por favor ingresar nombre ")
num1 = int(input(f"{nombre} ingrese el primer numero"))
num2 = int(input(f"{nombre} ingrese el segundo numero"))
#suma
suma = num1 + num2
print(f"la suma de {num1} + {num2} es: {suma}")
#resta
resta = num1 - num2
print(f"la resta de {num1} - {num2} es: {resta}")   
#multiplicacion
multiplicacion = num1 * num2
print(f"la multiplicacion de {num1} * {num2} es: {multiplicacion}") 
#division
division = num1 / num2
print(f"la division de {num1} / {num2} es: {division}")
#division entera
division_entera = num1 // num2
print(f"la division entera de {num1} // {num2} es: {division_entera}")
#modulo
modulo = num1 % num2
print(f"el modulo de {num1} % {num2} es: {modulo}")
#potencia
potencia = num1 ** num2
print(f"la potencia de {num1} ** {num2} es: {potencia}")