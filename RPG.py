# info a almacenar
# variable = entra al pueblo?
# si no entra = tiramos dados = sobrevive o no

print("-----------------------------------------------------------")
print("RPG version 0.0.1")
print("-----------------------------------------------------------")
print("Perteneces a la guardia. Llevas semanas caminando por la\n"
    "tundra en una expedición para detectar la presencia de \n"
    "posibles salvajes. Te has desmayado varias veces y el frío\n"
    "ha empezado a afectarte...")
jugador = input("recuerdas tu nombre?\n")
print(jugador + ", cierto...Cae la noche, llegas a un poblado con cinco\n"
    "cabañas, podrías entrar en una de ellas a descansar...\n"
    "pero corres el riesgo de encontrarte con un salvaje y morir.")

import random

cabañas = ["cabaña 1", "cabaña 2", "cabaña 3", "cabaña 4", "cabaña 5"]
interior = ("salvaje", "amigo", "desocupado")
seguir_jugando = "si"
mago =["si","no"]

eleccion_poblado = input("Te arriesgas a entrar en el poblado?\n")
if eleccion_poblado == "si":
    poblado = "si"
else:
    poblado = "no"
    mago = random.choice(mago)
    if mago == "si":
        print("Durante la noche un hombre con capa te encuentra y te lleva\n"
            "a su casa, parece un mago, pero estás demasiado cansado como para preguntar.")
    else:
        print("Tus escasas fuerzas no son suficientes para pasar la noche\n"
            "poco a poco te dejas arropar por el frío, no despertarás mañana.")

while seguir_jugando == "si" and poblado == "si":
    try:
        inp = (int(input("En cuál de las cabañas decices entrar?\n"))-1)
    except:
        print("Por favor, introduce un número del 1 al 5")
    cabañas[inp] = random.choice(interior)
    if cabañas[inp] == "salvaje":
        print("Abres la puerta lentamente. El interior está caliente\n"
        "y huele a comida; cruzas los dedos y sujetas tu daga con \n"
        "las manos entumecidas por el frío.\n"
        "De pronto, notas una sombra moviéndose a tu izquierda, alzas\n"
        "la daga pero tus dedos no resisten el peso y cae.\n"
        "La sombra se avalanza sobre ti. Es demasiado tarde.")
    elif cabañas[inp] == "amigo":
        print("Abres la puerta. La calidez del interior pone todos \n"
        "tus músculos en tensión; cruzas los dedos y sujetas tu daga\n"
        "con las manos entumecidas por el frío.\n"
        "Sentado a la mesa, un hombre te mira sorprendido:\n"
        "-Llevas el uniforme de la guardia, ¿eres uno de ellos o se lo\n has robado a un cadaver?\n"
        "Le exlicas tu situación, aún alerta, el hombre suelta una carcajada:\n"
        "-Qué, ¿quieres cenar? Me ha sobrado un poco de estofado.")

    else:
        print("Abres la puerta lentamente. El interior está casi\n"
        "tan frío como la calle, y una capa de polvo cubre toda la\n"
        "estancia.\n"
        "Por suerte, encuentras unas mantas raídas en uno de los cajones,\n"
        "y la cama no está tan maltrecha como parecía.\n"
        "Por fin tendrás una merecida noche de descanso")
    seguir_jugando = input("¿Quieres seguir jugando?\n")



    




  


