#! /usr/bin/python3
import math as m                 # Import modułu matematycznego jako "m" (np. m.pi)
import datetime as t            # Import modułu datetime jako "t"
import calendar as c            # Import modułu calendar jako "c"

# Stałe i zmienne globalne
constant1: int = 18
variable: int = 17
a: int = 1 #zmienna globalna a
A: int = 2 #zmienna globalna A (różni się wielkością liter)

# Główna funkcja programu
def main():
    pass


# # Zadanie 2 – pokazuje wersję zainstalowanego pythona
# def task2():
#     import pandas as pd                         # Import biblioteki pandas
#     print(pd.__version__)                       # Wyświetlenie wersji pandas
#
# # Zadanie 3 – pokazuje aktualną datę i czas w różnych formatach
# def task3():
#     now = t.datetime.now()                      # Aktualna data i godzina
#     current_time1 = now.strftime('%Y-%m-%d %H:%M:%S')     # Format 1
#     current_time2 = now.strftime('%d/%m/%Y, %I:%M %p')     # Format 2
#     current_time3 = now.strftime('%A, %d %B %Y, %H:%M')    # Format 3
#     print("format1:", current_time1)
#     print("format2:", current_time2)
#     print("format3:", current_time3)
#
# # Zadanie 4 – oblicza obwód i pole koła na podstawie promienia
# def task4():
#     promien = float(input("podaj promien: "))      # Pobranie promienia
#     ob = 2 * m.pi * promien                        # Obwód koła
#     pole = m.pi * promien ** 2                     # Pole koła
#     print("obwod wynosi:", ob)
#     print("pole wynosi:", pole)
#
# # Zadanie 5 – pokazuje różnicę między zmiennymi lokalnymi a globalnymi
def task5():
    a = 3 #lokalna zmienna 'a'
    A = 4 #lokalna zmienna 'A'
    print("w funkcji: ")
    print("wynik ", a, type(a)) #Wyświetlenie lokalnego 'a'
    print("wynik ", A, type(A)) #Wyświetlenie lokalnego 'A'

# Kod poza funkcją – pokazuje wartości zmiennych globalnych
print("poza funkcją")
print("wynik ", a, type(a)) #globalne 'a'
print("wynik ", A, type(A)) #globalne 'A'

# # # Zadanie 6 – pobiera imię i nazwisko i wypisuje w kolejności: nazwisko imię
# def task6():
#     name = input("whats your name? ")
#     surname = input("whats your surname? ")
#     return print(surname + " " + name)

# # Zadanie 7 – oblicza pierwiastki równania kwadratowego
# def task7():
#     j = int(input("liczba 1 "))   #współczynnik a
#     k = int(input("liczba 2 "))   #współczynnik b
#     l = int(input("liczba 3 ")) #współczynnik c
#     delta = k * k - 4 * j * l #obliczenie delty
#
#     if delta < 0:
#         print("brak rozwiazan") #brak pierwiastków
#     else:
#         delta = m.sqrt(delta)#pierwiastek z delty
#         x1 = (-k - delta) / (2 * j) #pierwszy pierwiastek
#         x2 = (-k + delta) / (2 * j) #drugi pierwiastek
#         if x1 > x2:
#             x1, x2 = x2, x1  #zamiana miejscami, jeśli trzeba
#         print(x1, x2)

# # Zadanie 8 – oblicza różnicę dni między dzisiejszą datą a 23.10.2025
# def task8():
#     data1 = t.date(2025, 10, 23)           # docelowa data
#     data2 = t.date.today()                 # dzisiejsza data
#     roznica = data1 - data2                # różnica w dniach
#     print("roznica dni:", roznica.days)

# # # Zadanie 9 – wyświetla kalendarz dla podanego miesiąca i roku
# def task9():
#     rok = int(input("rok "))
#     miesiac = int(input("miesiac "))
#     print(c.month(rok, miesiac))           # wyświetlenie kalendarza

# Zadanie 10 – wykonuje operacje arytmetyczne na dwóch liczbach
# def task10():
#     first_number = int(input("liczba 1 "))
#     second_number = int(input("liczba 2 "))
#     # print("dodawanie ", first_number + second_number)
#     # print("odejmowanie ", first_number - second_number)
#     # print("mnożenie", first_number * second_number)
#     # print("dzielenie", first_number / second_number)
#     # print("dzielenie całkowite", first_number // second_number)
#     # print("reszta z dzielenie", first_number % second_number)
#     # print("potęgowanie", first_number ** second_number)
#     print("dzielenie przez 0", (first_number + second_number) / 0)  #Błąd dzielenia przez zero

#Zadanie 11 – pokazuje kolejność wykonywania działań matematycznych
def task11():
    print("Przykład 9/3*2 ", 9 / 3 * 2) #mnożenie i dzielenie od lewej do prawej
    print("Przykład 2*3+5 ", 2 * 3 + 5) #najpierw mnożenie, potem dodawanie
    print("Przykład (3+5)*2 ", (3 + 5) * 2) #nawiasy mają najwyższy priorytet
    print("Przykład (2 * 2 * 3)) ", 2 * 2 * 3) #najpierw potęgowanie, potem mnożenie

# Zadanie 12 – różne przykłady dzielenia liczb całkowitych i zmiennoprzecinkowych
def task12():
    a = 1
    b = 2
    c = 3.5
    d = 4.5
#Dwie liczby całkowite
    print("wynik dzielenia dwóch liczb całkowitych: ", a / b)
    print("wynik dzielenia całkowitego dwóch liczb całkowitych", a // b)
    print("wynik dzielenia z resztą dwóch liczb całkowitych", a % b)
#Liczba całkowita i zmiennoprzecinkowa
    print("wynik dzielenia liczby całkowitej i zmiennoprzecinkowej: ", b / c)
    print("wynik dzielenia całkowitego liczby całkowitej i zmiennoprzecinkowej", b // c)
    print("wynik dzielenia z resztą liczby całkowitej i zmiennoprzecinkowej", b % c)
#Dwie liczby zmiennoprzecinkowe
    print("wynik dzielenia dwóch liczb zmiennoprzecinkowych: ", c / d)
    print("wynik dzielenia całkowitego dwóch liczb zmiennoprzecinkowych", c // d)
    print("wynik dzielenia z resztą dwóch liczb zmiennoprzecinkowych", c % d)

# Wywołanie wszystkich funkcji po kolei
main()
# task2()
# task3()
# task4()
task5()
# task6()
# task7()
# task8()
# task9()
# task10()
# task11()
# task12()