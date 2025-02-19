
nombre1 = input("Jugador 1, ¿cómo te llamas? ")
nombre2 = input("Jugador 2, ¿cómo te llamas? ")

turnos = 3
ronda = 1
puntos1 = 0

puntos2 = 0


while ronda <=  turnos:
    print(f"Ronda {ronda}")


    jugador1 = input(f"hola {nombre1} 1: ¿piedra, papel o tijeras?") .lower()
    jugador2 = input(f"hola {nombre2} 2: ¿piedra, papel o tijeras?") .lower()


    condicionA = jugador1 == "piedra" and jugador2 == "tijeras" or jugador1 == "tijeras" and jugador2 == "papel" or jugador1 == "papel" and jugador2 == "piedra"

    if jugador1 == jugador2:
     print("Empate")
    elif condicionA:
        print("Ha ganado", nombre1)
        puntos1 += 1
    else:
        print("Ha ganado", nombre2)
        puntos2 += 1
    # Incrementar el número de ronda   
    ronda += 1

# Determinar el ganador final
print("\nResultados finales:")
print(f"{nombre1}: {puntos1} puntos")
print(f"{nombre2}: {puntos2} puntos")