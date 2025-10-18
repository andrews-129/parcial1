#Escribe un programa que pida al usuario una frase y muestre cuál es la palabra más larga junto con su longitud.
frase = input("Escribe una frase: ")
palabras = frase.split()

palabra_larga = ""
longitud = 0

for palabra in palabras:
    if len(palabra) > longitud:
        palabra_larga = palabra
        longitud = len(palabra)

print("La palabra más larga es: ", palabra_larga)
print("La longitud es: ", longitud)

#Crea un programa que determine si un número ingresado por el usuario es un número perfecto (la suma de sus divisores propios es igual al número).
num = int(input("Ingrese el numero: "))
sum_div = 0
for i in range (1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print("El numero ", str(num), " es perfecto")
else:

    print("El numero ", str(num), " no es perfecto")
