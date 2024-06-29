print("estes es un proyecto de operaciones matematicas verifica si un numero x es menor o igual que un numero y")
nombre = input("por favor ingresar nombre ")
num1 = int(input(f"{nombre} ingrese el numero x"))
num2 = int(input(f"{nombre} ingrese el numero y"))
menorigual = num1 <= num2
print(f"{nombre} los numeros {num1} y {num2} son {menorigual}")