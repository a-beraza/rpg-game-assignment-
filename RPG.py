# info a almacenar
# nombre del jugador
# tupla = posibilidades de cabaña
# variable = entra al pueblo?
# si no entra = tiramos dados = sobrevive o no
# variable = cabaña que elige [1-5]
# volver a jugar?
import random

jugador = input ("Nombre: ")

interior_cabaña = ("salvaje","amigo","desocupado")

jugar = "si"

while jugar == "si": 
    cabaña_1 = random.choice(interior_cabaña)
    cabaña_2 = random.choice(interior_cabaña)
    cabaña_3 = random.choice(interior_cabaña)
    cabaña_4 = random.choice(interior_cabaña)
    cabaña_5 = random.choice(interior_cabaña)
    cabaña_usuario = int(input("Escoge una cabaña: "))
    if cabaña_usuario == 1:
        print(cabaña_1)
    elif cabaña_usuario == 2:
        print(cabaña_2)
    elif cabaña_usuario == 3:
        print(cabaña_3)
    elif cabaña_usuario == 4:
        print(cabaña_4)
    else:
        print(cabaña_5)
    jugar = input("Quieres seguir jugando? si/no: ")

print("Tu misión ha terminado")