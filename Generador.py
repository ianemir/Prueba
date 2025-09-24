import random

caracters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Ingrese la longitud de la contraseña: "))

password = ""  

for i in range(longitud):
    password += random.choice(caracters)
print("Tu contraseña es: " + password)
