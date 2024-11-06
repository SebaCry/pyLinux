import random


def choose_options():
    opciones = ('piedra', 'papel', 'tijera')
    
    user_opciones = input('Escoje piedra papel o tijera => ').lower()
    computador_opcion = random.choice(opciones)
    
    if not user_opciones in opciones:
        print('Opcion no valida :(')
        return None, None
    
    print(f'La lucha esta entre: {user_opciones} y {computador_opcion}')

    return user_opciones, computador_opcion

def run_game():
    rounds = 0
    user_vidas = 3
    computador_vidas = 3

    while True:
        user_opcion, computador_opcion = choose_options()

        if user_opcion == computador_opcion:
            rounds += 1
            print('Nadieee gana, continue el JUEGOOOO')

        if (user_opcion == 'piedra' and computador_opcion == 'tijera') or (user_opcion == 'papel' and computador_opcion == 'piedra') or (user_opcion == 'tijera' and computador_opcion == 'papel'):
            rounds += 1
            computador_vidas -= 1
            print(f'El jugador le gana al computador, y el computador tiene: {computador_vidas} vidas')

        if (user_opcion == 'piedra' and computador_opcion == 'papel') or (user_opcion == 'papel' and computador_opcion == 'tijera') or (user_opcion == 'tijera' and computador_opcion == 'piedra'):
            rounds += 1
            user_vidas -= 1


        if rounds == 3:
            if user_vidas == computador_vidas:
                print('Empateeeeeeee')
                break

            if user_vidas > computador_vidas:
                print(f'El ganador del juego es el JUGADORRR')
                break
            else:
                print(f'El ganador es el computadorrrr')
                break

if __name__ == "__main__":
    run_game()