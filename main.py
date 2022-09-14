import random
import sys
import time

colors = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "RESET": "\033[39m",
}

questions = {
    0: {
        "question": "¿Quién fue el creador de windows?",
        "answer": "Bill Gates",
        "options":
        ["Bill Gates", "Billy Gates", "Bill Dates", "Billy Bill Gate"]
    },
    1: {
        "question":
        "¿Quién fue el creador de Linux?",
        "answer":
        "Linus Torvalds",
        "options": [
            "Linus Torvalds", "Linux Torvalds", "Linu Torvalds",
            "Linus Trovalds"
        ]
    },
    2: {
        "question": "¿Quién fue el creador de Apple?",
        "answer": "Steve Jobs",
        "options": ["Steve Jobs", "Steven Jobs", "Steve Bojs", "Steve Job"]
    },
    3: {
        "question": "¿Quién fue el creador de Google?",
        "answer": "Larry Page",
        "options": ["Larry Page", "Larry Pages", "Lars Page", "Lard Pages"]
    },
    4: {
        "question": "¿Quién fue el creador de Tesla?",
        "answer": "Elon Musk",
        "options": ["Elon Musk", "Elon Mus", "Elon Must", "Elonn Musk"]
    },
    5: {
        "question":
        "¿Quiénes fueron los creadores de Youtube?",
        "answer":
        "Steve Chen, Jawed Karim y Chad Hurley",
        "options": [
            "Steve Chen, Jawed Karim y Chad Hurley",
            "Steve Chad, Jawel Karim y Chad Hurley",
            "Steve Chin, Jawe Karim y Chad Hurles",
            "Steve Chen, Jawed Karim y Chad Hurlley"
        ]
    },
    6: {
        "question":
        "¿Quién fue el creador de Python?",
        "answer":
        "Guido van Rossum",
        "options": [
            "Guido van Rossum", "Guido van Rossia", "Guido van Ross",
            "Guido van der Geld"
        ]
    },
    7: {
        "question": "¿Quién fue el creador de Javascript?",
        "answer": "Brendan Eich",
        "options":
        ["Brendan Eich", "Brendan Eichs", "Brend Eich", "Brendans Eich"]
    },
    8: {
        "question":
        "¿Quiénes fueron los creadores de Instagram?",
        "answer":
        "Kevin Systrom y Mike Krieger",
        "options": [
            "Kevin Systrom y Mike Krieger", "Kevin Systrem y Mike Kriegerz",
            "Kevin Systr y Mikes Krier", "Kev Systrom y Michael Krieger"
        ]
    }
}

numbers = []

for times in range(0, len(questions)):
    numbers.append(times)

random.shuffle(numbers)

for question_number in questions.keys():
    random.shuffle(questions[question_number]["options"])

valid_answers = ['a', 'b', 'c', 'd', 'e']

name = input(
    f"{colors['BLUE']}      ******************************************************************\n      *  Bienvenido al juego de trivia, ingresa tu nombre para iniciar *\n      ******************************************************************\n{colors['RESET']}name: "
).capitalize().strip()

print(
    f"\n Hola, {name}, ahora selecciona el nivel de juego, en el nivel fácil tendrás 3 oportunidades para probar tu respuesta, en el nivel medio tendrás 2 oportunidades y en el nivel difícil tendrás sólo una oportunidad.\n"
)
keep_playing = True
try_time = 1
while keep_playing == True:
    points = 0
    print("\na) Nivel fácil (Tendrás 3 oportunidades por pregunta)")
    print("b) Nivel medio (Tendrás 2 oportunidades por pregunta)")
    print("c) Nivel difícil (Tendrás sólo 1 oportunidad por pregunta)")
    print("d) Salir\n")

    option = input("Elige una opción: ")

    while option not in valid_answers:
        option = input(
            f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(a-b-c-d): {colors['RESET']}"
        ).lower()

    if option == "d":
        sys.exit(
            f"{colors['BLUE']}Gracias por participar, hasta la próxima!{colors['RESET']}"
        )
    elif option == "a":
        print(f"\nIntento número: {try_time}")
        print(
            "\nElegiste el nivel fácil, selecciona la opción correcta (a-b-c-d) y presiona la tecla Enter para continuar"
        )
        for times in range(0, len(questions)):
            lifes = 3
            while lifes != 0:
                print(
                    f"\n{colors['CYAN']}{times +1}) {questions[numbers[times]]['question']}{colors['RESET']}"
                )
                print(f"a) {questions[numbers[times]]['options'][0]}")
                print(f"b) {questions[numbers[times]]['options'][1]}")
                print(f"c) {questions[numbers[times]]['options'][2]}")
                print(f"d) {questions[numbers[times]]['options'][3]}")
                answer = input("\nIngresa tu respuesta: ")
                while answer.lower() not in valid_answers:
                    answer = input(
                        f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(a-b-c-d): {colors['RESET']}"
                    )
                if answer == 'a':
                    if questions[numbers[times]]['answer'] == questions[
                            numbers[times]]['options'][0]:
                        print(
                            f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                        )
                        points += 1
                        lifes = 0
                        time.sleep(2)
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, ya no te quedan más intentos para esta pregunta{colors['RESET']}\n"
                            )
                            time.sleep(2)
                        else:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, intentos restantes = {lifes}{colors['RESET']}\n"
                            )
                            time.sleep(2)
                elif answer == 'b':
                    if questions[numbers[times]]['answer'] == questions[
                            numbers[times]]['options'][1]:
                        print(
                            f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                        )
                        points += 1
                        lifes = 0
                        time.sleep(2)
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, ya no te quedan más intentos para esta pregunta{colors['RESET']}\n"
                            )
                            time.sleep(2)
                        else:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, intentos restantes = {lifes}{colors['RESET']}\n"
                            )
                            time.sleep(2)
                elif answer == 'c':
                    if questions[numbers[times]]['answer'] == questions[
                            numbers[times]]['options'][2]:
                        print(
                            f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                        )
                        points += 1
                        lifes = 0
                        time.sleep(2)
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, ya no te quedan más intentos para esta pregunta{colors['RESET']}\n"
                            )
                            time.sleep(2)
                        else:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, intentos restantes = {lifes}{colors['RESET']}\n"
                            )
                            time.sleep(2)
                elif answer == 'd':
                    if questions[numbers[times]]['answer'] == questions[
                            numbers[times]]['options'][3]:
                        print(
                            f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                        )
                        points += 1
                        lifes = 0
                        time.sleep(2)
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, ya no te quedan más intentos para esta pregunta{colors['RESET']}\n"
                            )
                            time.sleep(2)
                        else:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, intentos restantes = {lifes}{colors['RESET']}\n"
                            )
                            time.sleep(2)
                elif answer == 'e':  #Respuesta secreta (comodín)
                    print(
                        f"{colors['GREEN']}\nRespuesta secreta fue encontrada, respuesta correcta, felicidades!{colors['RESET']}\n"
                    )
                    points += 1
                    lifes = 0
                    time.sleep(2)
            else:
                continue
        keep_playing_valid = ["y", "n"]
        if points == 0:
            print(
                f"\n{colors['BLUE']}{name}, no lograste acumular puntos, no te rindas, sigue practicando!{colors['RESET']}"
            )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
        elif points == 1:
            print(
                f"\n{colors['BLUE']}Felicidades, {name}, acumulaste {points} punto!{colors['RESET']}"
            )
            roulette = input(
                f"\n{colors['BLUE']}{name}, tienes la oportunidad de girar una ruleta para conseguir duplicar tus puntos, si esta falla, recuerda que perderás tus puntos acumulados.\nPresiona Y para aceptar o N para conservar tus puntos actuales{colors['RESET']}: "
            ).lower()
            while roulette not in keep_playing_valid:
                roulette = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if roulette == "y":
                random_number = random.randint(1, 3)
                if random_number == 1:
                    points = points * 2
                    print(
                        f"\n{colors['BLUE']}Felicidades, {name}, ganaste en la ruleta y ahora tienes {points} puntos!{colors['RESET']}"
                    )
                else:
                    print(
                        f"\n{colors['RED']}{name}, la ruleta falló y te quedaste sin puntos :({colors['RESET']}"
                    )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
        else:
            print(
                f"\n{colors['BLUE']}Felicidades, {name}, acumulaste {points} puntos!{colors['RESET']}"
            )
            roulette = input(
                f"\n{colors['BLUE']}{name}, tienes la oportunidad de girar una ruleta para conseguir duplicar tus puntos, si esta falla, recuerda que perderás tus puntos acumulados.\nPresiona Y para aceptar o N para conservar tus puntos actuales{colors['RESET']}: "
            ).lower()
            while roulette not in keep_playing_valid:
                roulette = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if roulette == "y":
                random_number = random.randint(1, 3)
                if random_number == 1:
                    points = points * 2
                    print(
                        f"\n{colors['BLUE']}Felicidades, {name}, ganaste en la ruleta y ahora tienes {points} puntos!{colors['RESET']}"
                    )
                else:
                    print(
                        f"\n{colors['RED']}{name}, la ruleta falló y te quedaste sin puntos :({colors['RESET']}"
                    )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
    elif option == "b":
        print(f"\nIntento número: {try_time}")
        print(
            "\nElegiste el nivel medio, selecciona la opción correcta (a-b-c-d) y presiona la tecla Enter para continuar"
        )
        for times in range(0, len(questions)):
            lifes = 2
            while lifes != 0:
                print(
                    f"\n{colors['CYAN']}{times +1}) {questions[numbers[times]]['question']}{colors['RESET']}"
                )
                print(f"a) {questions[numbers[times]]['options'][0]}")
                print(f"b) {questions[numbers[times]]['options'][1]}")
                print(f"c) {questions[numbers[times]]['options'][2]}")
                print(f"d) {questions[numbers[times]]['options'][3]}")
                answer = input("\nIngresa tu respuesta: ")
                while answer.lower() not in valid_answers:
                    answer = input(
                        f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(a-b-c-d): {colors['RESET']}"
                    )
                if answer == 'a':
                    if questions[numbers[times]]['answer'] == questions[
                            numbers[times]]['options'][0]:
                        points += 1
                        lifes = 0
                        print(
                            f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                        )
                        time.sleep(2)
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, ya no te quedan más intentos para esta pregunta{colors['RESET']}\n"
                            )
                            time.sleep(2)
                        else:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, intentos restantes = {lifes}{colors['RESET']}\n"
                            )
                            time.sleep(2)
                elif answer == 'b':
                    if questions[numbers[times]]['answer'] == questions[
                            numbers[times]]['options'][1]:
                        points += 1
                        lifes = 0
                        print(
                            f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                        )
                        time.sleep(2)
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, ya no te quedan más intentos para esta pregunta{colors['RESET']}\n"
                            )
                            time.sleep(2)
                        else:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, intentos restantes = {lifes}{colors['RESET']}\n"
                            )
                            time.sleep(2)
                elif answer == 'c':
                    if questions[numbers[times]]['answer'] == questions[
                            numbers[times]]['options'][2]:
                        points += 1
                        lifes = 0
                        print(
                            f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                        )
                        time.sleep(2)
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, ya no te quedan más intentos para esta pregunta{colors['RESET']}\n"
                            )
                            time.sleep(2)
                        else:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, intentos restantes = {lifes}{colors['RESET']}\n"
                            )
                            time.sleep(2)
                elif answer == 'd':
                    if questions[numbers[times]]['answer'] == questions[
                            numbers[times]]['options'][3]:
                        points += 1
                        lifes = 0
                        print(
                            f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                        )
                        time.sleep(2)
                    else:
                        lifes -= 1
                        if lifes == 0:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, ya no te quedan más intentos para esta pregunta{colors['RESET']}\n"
                            )
                            time.sleep(2)
                        else:
                            print(
                                f"{colors['RED']}\nRespuesta incorrecta, intentos restantes = {lifes}{colors['RESET']}\n"
                            )
                            time.sleep(2)
                elif answer == 'e':  #Respuesta secreta (comodín)
                    print(
                        f"{colors['GREEN']}\nRespuesta secreta fue encontrada, respuesta correcta, felicidades!{colors['RESET']}\n"
                    )
                    points += 1
                    lifes = 0
                    time.sleep(2)
            else:
                continue
        keep_playing_valid = ["y", "n"]
        if points == 0:
            print(
                f"\n{colors['BLUE']}{name}, no lograste acumular puntos, no te rindas, sigue practicando!{colors['RESET']}"
            )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
        elif points == 1:
            print(
                f"\n{colors['BLUE']}Felicidades, {name}, acumulaste {points} punto!{colors['RESET']}"
            )
            roulette = input(
                f"\n{colors['BLUE']}{name}, tienes la oportunidad de girar una ruleta para conseguir duplicar tus puntos, si esta falla, recuerda que perderás tus puntos acumulados.\nPresiona Y para aceptar o N para conservar tus puntos actuales{colors['RESET']}: "
            ).lower()
            while roulette not in keep_playing_valid:
                roulette = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if roulette == "y":
                random_number = random.randint(1, 3)
                if random_number == 1:
                    points = points * 2
                    print(
                        f"\n{colors['BLUE']}Felicidades, {name}, ganaste en la ruleta y ahora tienes {points} puntos!{colors['RESET']}"
                    )
                else:
                    print(
                        f"\n{colors['RED']}{name}, la ruleta falló y te quedaste sin puntos :({colors['RESET']}"
                    )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
        else:
            print(
                f"\n{colors['BLUE']}Felicidades, {name}, acumulaste {points} puntos!{colors['RESET']}"
            )
            roulette = input(
                f"\n{colors['BLUE']}{name}, tienes la oportunidad de girar una ruleta para conseguir duplicar tus puntos, si esta falla, recuerda que perderás tus puntos acumulados.\nPresiona Y para aceptar o N para conservar tus puntos actuales{colors['RESET']}: "
            ).lower()
            while roulette not in keep_playing_valid:
                roulette = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if roulette == "y":
                random_number = random.randint(1, 3)
                if random_number == 1:
                    points = points * 2
                    print(
                        f"\n{colors['BLUE']}Felicidades, {name}, ganaste en la ruleta y ahora tienes {points} puntos!{colors['RESET']}"
                    )
                else:
                    print(
                        f"\n{colors['RED']}{name}, la ruleta falló y te quedaste sin puntos :({colors['RESET']}"
                    )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
    else:
        print(f"\nIntento número: {try_time}")
        print(
            "\nElegiste el nivel difícil, selecciona la opción correcta (a-b-c-d) y presiona la tecla Enter para continuar"
        )
        for times in range(0, len(questions)):
            print(
                f"\n{colors['CYAN']}{times +1}) {questions[numbers[times]]['question']}{colors['RESET']}"
            )
            print(f"a) {questions[numbers[times]]['options'][0]}")
            print(f"b) {questions[numbers[times]]['options'][1]}")
            print(f"c) {questions[numbers[times]]['options'][2]}")
            print(f"d) {questions[numbers[times]]['options'][3]}")
            answer = input("\nIngresa tu respuesta: ")
            while answer.lower() not in valid_answers:
                answer = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(a-b-c-d): {colors['RESET']}"
                )
            if answer == 'a':
                if questions[numbers[times]]['answer'] == questions[
                        numbers[times]]['options'][0]:
                    points += 1
                    print(
                        f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                    )
                    time.sleep(2)
                    continue
                else:
                    print(
                        f"{colors['RED']}\nRespuesta incorrecta{colors['RESET']}\n"
                    )
                    time.sleep(2)
                    continue
            elif answer == 'b':
                if questions[numbers[times]]['answer'] == questions[
                        numbers[times]]['options'][1]:
                    points += 1
                    print(
                        f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                    )
                    time.sleep(2)
                    continue
                else:
                    print(
                        f"{colors['RED']}\nRespuesta incorrecta{colors['RESET']}\n"
                    )
                    time.sleep(2)
                    continue
            elif answer == 'c':
                if questions[numbers[times]]['answer'] == questions[
                        numbers[times]]['options'][2]:
                    points += 1
                    print(
                        f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                    )
                    time.sleep(2)
                    continue
                else:
                    print(
                        f"{colors['RED']}\nRespuesta incorrecta{colors['RESET']}\n"
                    )
                    time.sleep(2)
                    continue
            elif answer == 'd':
                if questions[numbers[times]]['answer'] == questions[
                        numbers[times]]['options'][3]:
                    points += 1
                    print(
                        f"{colors['GREEN']}\nRespuesta correcta, felicidades!{colors['RESET']}\n"
                    )
                    time.sleep(2)
                    continue
            elif answer == 'e':  #Respuesta secreta (comodín)
                print(
                    f"{colors['GREEN']}\nRespuesta secreta fue encontrada, respuesta correcta, felicidades!{colors['RESET']}\n"
                )
                points += 1
                lifes = 0
                time.sleep(2)
            else:
                print(
                    f"{colors['RED']}\nRespuesta incorrecta{colors['RESET']}\n"
                )
                time.sleep(2)
                continue
        keep_playing_valid = ["y", "n"]
        if points == 0:
            print(
                f"\n{colors['BLUE']}{name}, no lograste acumular puntos, no te rindas, sigue practicando!{colors['RESET']}"
            )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
        elif points == 1:
            print(
                f"\n{colors['BLUE']}Felicidades, {name}, acumulaste {points} punto!{colors['RESET']}"
            )
            roulette = input(
                f"\n{colors['BLUE']}{name}, tienes la oportunidad de girar una ruleta para conseguir duplicar tus puntos, si esta falla, recuerda que perderás tus puntos acumulados.\nPresiona Y para aceptar o N para conservar tus puntos actuales{colors['RESET']}: "
            ).lower()
            while roulette not in keep_playing_valid:
                roulette = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if roulette == "y":
                random_number = random.randint(1, 3)
                if random_number == 1:
                    points = points * 2
                    print(
                        f"\n{colors['BLUE']}Felicidades, {name}, ganaste en la ruleta y ahora tienes {points} puntos!{colors['RESET']}"
                    )
                else:
                    print(
                        f"\n{colors['RED']}{name}, la ruleta falló y te quedaste sin puntos :({colors['RESET']}"
                    )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
        else:
            print(
                f"\n{colors['BLUE']}Felicidades, {name}, acumulaste {points} puntos!{colors['RESET']}"
            )
            roulette = input(
                f"\n{colors['BLUE']}{name}, tienes la oportunidad de girar una ruleta para conseguir duplicar tus puntos, si esta falla, recuerda que perderás tus puntos acumulados.\nPresiona Y para aceptar o N para conservar tus puntos actuales{colors['RESET']}: "
            ).lower()
            while roulette not in keep_playing_valid:
                roulette = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if roulette == "y":
                random_number = random.randint(1, 3)
                if random_number == 1:
                    points = points * 2
                    print(
                        f"\n{colors['BLUE']}Felicidades, {name}, ganaste en la ruleta y ahora tienes {points} puntos!{colors['RESET']}"
                    )
                else:
                    print(
                        f"\n{colors['RED']}{name}, la ruleta falló y te quedaste sin puntos :({colors['RESET']}"
                    )
            time.sleep(2)
            keep_playing_option = input(
                "\nDeseas seguir jugando?. Presiona Y para sí o N para No: "
            ).lower()
            while keep_playing_option not in keep_playing_valid:
                keep_playing_option = input(
                    f"{colors['YELLOW']}\nRespuesta no válida, ingresa una respuesta válida(y-n): {colors['RESET']}"
                ).lower()
            if keep_playing_option == "n":
                keep_playing = False
            else:
                try_time += 1
else:
    sys.exit(
        f"{colors['BLUE']}Gracias por participar, hasta la próxima!{colors['RESET']}"
    )
