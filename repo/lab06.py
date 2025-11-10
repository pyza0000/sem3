#zadanie 1 ___________________________
# def choose_base():
#     while True:
#         base = input("Podstawa systemu liczbowego ")
#         if base in ['2','8','10','16']:
#             return int(base)
#         else:
#             print("nieprawidlowa wartosc")
#
# def choose_number(base):
#     while True:
#         number = input("Podaj liczbe ")
#         try:
#             number_dec = int(number,base)
#             return number_dec
#         except ValueError:
#             print("nieprawidlowa wartosc")
# def main():
#     base = choose_base()
#     number_dec = choose_number(base)
#     print(f"dwojkowo {bin(number_dec)[2:]}")
#     print(f"dziesietnie {number_dec}")
#     print(f"osemkowo {oct(number_dec)[2:]}")
#     print(f"szesnastkowo {hex(number_dec)[2:].upper()}")


import random

#zadanie 2_____________________________
# def task2():
#     while True:
#         number = int(input("give me number: "))
#         if number > 255 or number < 0:
#             return 0
#         else:
#             index = int(input("give me index of bits: "))
#         return print(f"dla wartości {number},{index} otrzymamy {(number >>index) & 1}"
#                      f", bo {number} = {bin(number)[2:]}")

#zadanie 3________________________________
# import random
# import math as m
# def task3():
#     numbers = []
#     for i in range(3):
#         number = random.randint(3, 11)
#         numbers.append(number)
#         print(number)
#     if numbers[0] + numbers[1] > numbers[2] and numbers[0] + numbers[2] > numbers[1] and numbers[1] + numbers[2] > numbers[0]:
#         print("trójkąt może powstać")
#     else:
#         return print("trójkąt nie może powstać")
#     s = (numbers[0] + numbers[1] + numbers[2]) / 2
#     p = m.sqrt(s*(s-numbers[0])*(s-numbers[1])*(s-numbers[2]))
#     print(f"pole: {p:.3f}")

#zadanie 4___________________
# def task4():
#     winnings = 0
#     attempts = 0
#     while True:
#         voice = str(input("orzel czy reszka? | wyjscie=x "))
#         lottery_words = ["orzel", "reszka"]
#         if voice in ["orzel", "reszka"]:
#             random_word = random.choice(lottery_words)
#             if voice == random_word:
#                 print("Dobrze trafiłeś!!!", voice)
#                 winnings += 1
#                 attempts += 1
#             else:
#                 print("spróbuj jeszcze raz")
#                 attempts += 1
#         elif voice == "x":
#             return print(f"próby: {attempts} wygrane: {winnings}")
#         else:
#             print("wybierz jedną z 3 opcji")

#zadanie 5_____________________________-
# def task5():
#     winnings = 0
#     attempts = 0
#     while True:
#         selected = str(input("papier/kamien czy nozyce? | wyjscie=x "))
#         lottery_words = ["papier","kamien","nozyce"]
#         if selected in ['papier','kamien','nozyce']:
#             random_selected = random.choice(lottery_words)
#             if selected == random_selected:
#                 print("wygrales!", random_selected)
#                 winnings += 1
#                 attempts += 1
#             else:
#                 print("sprobuj jeszcze raz")
#                 attempts += 1
#         elif(selected == 'x'):
#             return print(f"próby: {attempts} wygrane: {winnings}")
#         else:
#             print("niepoprawny wybor opcji")

#zadanie 6________________
# import math
# def task6(angle,ladder_length):
#     angle = math.radians(angle)
#     length = ladder_length * math.sin(angle)
#     return length
#
# def main():
#     angle = float(input("Podaj kąt: "))
#     ladder_length = float(input("Podaj długość drabiny: "))
#     result = task6(angle,ladder_length)
#     print(f"Wysokość na jaką sięga koniec drabiny: {result:.2f}")

#zadanie 7__________________
def task7():
    result = ""
    for i in range(0,91):



if __name__ == '__main__':
    main()
    # task2()
    # task3()
    # task4()
    # task5()
