'''
    UBA XXI - Pensamiento Computacional TP 3 - Ivan Andrade
    -------------------------------------------------------

    Ejercicio 5.
         Juego de Piedra, papel o tigera. Vos vs
         la maquina.
'''
import random

play_words = ['r', 'p', 't']
user_word = None
random_word = None
game_over = False

point_user = 0
point_machine = 0

#Genera letras random
def letra_aleatoria(words):
    return random.choice(words)


#Compara letras user y machine.
def comparar_letras(machine_words, user_words):
    global point_user
    global point_machine

    if machine_words == user_words:
        pass
    elif (user_words == "r" and machine_words == "t") or (user_words == "p" and machine_words == "r") or (user_words == "t" and machine_words == "p"):
        point_user = point_user +  1
    else:
        point_machine = point_machine + 1

#Pide los datos
def input_data():
    salir = True
    global user_word
    global game_over
    while salir:
        user_word  = input("Piedra[r], papel[p] o tijera[t], para Salir[q]: ")
        if user_word in play_words:
                        break
        elif user_word == 'q':
            print("¡Hasta luego, gracias por jugar!")
            game_over = True
            break
        else:
            print("Ingrese una letra valida")

def main():
    global game_over
    # Imprime resultados y llama a las funciones
    while not game_over and point_machine != 3 and point_user != 3:
        input_data()
        if game_over:
             break
        random_word = letra_aleatoria(play_words)
        comparar_letras(random_word, user_word)
        print("Maquina: ", random_word)
        print("Tus puntos: ", point_user)
        print("Puntos maquina: ", point_machine)
   
    if point_user == 3:
        print("¡Felicitaciones, ganaste!")
    elif point_machine == 3:
        print("Segui participando jaja")


if __name__ == "__main__":
    main()
