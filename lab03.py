# #zadanie 1
# list = [] #Tworzenie pustej listy
# list.extend([0,1,2,3,4]) #Dodanie kilku elementów naraz do listy
# print("Pierwsze 2 elementy:", list[:2]) #Wypisanie dwóch pierwszych elementów (indeksy 0 i 1)
# print("Ostatnie 2 elementy:", list[-2:]) #Wypisanie dwóch ostatnich elementów
# print("dlugosc", len(list)) #Wypisanie długości listy
# print("parzyste  elementy:", list[::2]) #Wypisanie co drugiego elementu (od 0)
# list.append(5) #Dodanie elementu 5 na koniec listy
# # list.append("almostdecember") #Dodanie napisu do listy
# print(list)
# list.sort(reverse=True) #Posortowanie listy malejąco
# print(list)
# list.pop(-1)  # Usunięcie ostatniego elementu z listy
# print(list)w
# list.insert(2,13) #Wstawienie liczby 13 na pozycję o indeksie 2
# print(list)
# my_counts = list.count(13) #Zliczenie ile razy 13 występuje w liście
# print(my_counts)

# #zadanie 2
# def task2():
#     list1 = [] #Pusta lista na liczby
#     for i in range(10): #Pętla 10 razy
#         number = int(input("give me number:")) #Pobranie liczby od użytkownika
#         list1.append(number) #Dodanie liczby do listy
#     print(list1)
#     list1.sort() #Sortowanie listy rosnąco
#     print("najmniejszy element ",list1[0]) #Pierwszy element po sortowaniu to najmniejszy
#     print("najwiekszy element element ",list1[-1]) #Ostatni to największy
#     non_negative = [x for x in list1 if x >= 0] #Wybranie tylko liczb nieujemnych
#     if non_negative:
#         srednia = sum(non_negative) / len(non_negative) #Obliczenie średniej
#     else:
#         srednia = 0 #Jeśli nie ma liczb nieujemnych – średnia = 0
#     print("Średnia liczb nieujemnych:", srednia)
# task2()
import random
#zadanie 3
def task3():
    list3_1 = []
    list3_2 = []
    for num in range(1, 6):
        list3_1.append(random.randint(1, 6)) #Losowanie 5 liczb z zakresu 1–6
        list3_2.append(random.randint(1, 6))
    print(list3_1)
    print(list3_2)
    unique = [element for element in list3_1 if element not in list3_2]
    print(unique)
task3()
#zadanie 4
def task4():
    list4 = []
    for i in range(10):
        list4.append(random.randint(1,10)) #Losowanie 10 liczb od 1 do 10
    print(list4)
    odd = [element for element in list4 if element%2 != 0] #Wybranie tylko nieparzystych
    print("jedynie liczby nieparzyste: ",odd)
    odd.sort() #Sortowanie listy
    print("najmniejszy element ", odd[0])
task4()
# #zadanie 5
# def task5():
#     list_A = [1,2,3]
#     list_B = [4,5,6]
#     list_AB = list_A + list_B #Połączenie list
#     print(list_AB)
#     list_BA = []
#     list_BA = list_B.copy() #Kopiowanie listy B
#     list_BA.extend(list_A) #Dodanie elementów listy A do B
#     print(list_BA)
# task5()
#zadanie 6
# def task6():
#     numbers = []
#     value = 1
#     while(value):
#         number = int(input("Enter a number: ")) #Pobranie liczby od użytkownika
#         if number == 0: #Jeśli liczba 0 – koniec programu
#             break
#         numbers.append(number) #Dodanie liczby do zbioru (duplikaty się nie dodadzą)
#         unique = set(numbers)
#         print("unikatowe elementy: ",unique)
# task6()
# #zadanie 7
# def task7():
#     tuple = ("apple", "banana", "cherry")
#     tuple_b = ("orange",)
#     tuple += tuple_b #dodawanie krotek
#     print("dodawanie krotki: ", tuple)
#     multi_tuple = tuple * 2 #mnożenie krotek
#     print("mnozenie krotek: ",multi_tuple)
#     print("dlugosc krotki:", len(tuple)) #długość krotki - liczba elementów
#     for x in tuple: #wypisanie wszystkich elementów krotki
#         print(x)
# task7()
# #zadanie8
# def task8():
#     the_set8 = set(["Marchew","Pomidor","Ogórek","Papryka","Brokuł"])
#     # the_set8.remove("banana")  # usunięcie nieistniejącego elementu =  błąd
#     # the_set8.discard("banana")  # usunięcie nieistniejącego elementu = nawet jesli go nie ma, to dziala normalnie
#     the_set8.pop() #Usunięcie losowego elementu
#     for x in the_set8:
#         print(x)
# task8()
# #zadanie 9
# def task9():
#     set9_1 = set(random.sample(range(1, 10), 3))
#     set9_2 = set(random.sample(range(1, 10), 3))
#     print("Zbiory:")
#     print(f"set9_1: {set9_1}")
#     print(f"set9_2: {set9_2}\n")
#     result_a = set9_1.isdisjoint(set9_2) #Sprawdza, czy zbiory nie mają żadnych wspólnych elementów.
#     print(f"a. isdisjoint: {result_a}, type: {type(result_a)}")
#     result_b = set9_1.issubset(set9_2) #Sprawdza, czy wszystkie elementy set9_1 znajdują się w set9_2.
#     print(f"b. issubset: {result_b}, type: {type(result_b)}")
#     result_c = set9_1.issuperset(set9_2)#Sprawdza, czy set9_1 zawiera wszystkie elementy set9_2.
#     print(f"c. issuperset: {result_c}, type: {type(result_c)}")
#     result_d = set9_1.union(set9_2) #Tworzy nowy zbiór, który zawiera wszystkie elementy z obu zbiorów (bez duplikatów).
#     print(f"d. union: {result_d}, type: {type(result_d)}")
#     result_e = set9_1.difference(set9_2) #Zwraca elementy, które są tylko w set9_1, ale nie w set9_2.
#     print(f"e. difference: {result_e}, type: {type(result_e)}")
#     result_f = set9_1.intersection(set9_2) #Zwraca część wspólną zbiorów – elementy, które występują w obu zbiorach.
#     print(f"f. intersection: {result_f}, type: {type(result_f)}")
# task9()
# #zadanie 10
# def task10():
#     car_dict = {
#         "brand": "Ford",
#         "model": "Mustang",
#         "year": 1964,
#         "new": False
#     }
#     car_dict["color"] = "red" #Dodanie nowego klucza
#     car_dict["year"] = 2020 #Zmiana istniejącej wartości
#     car_dict.pop("new") #Usunięcie klucza 'new'
#     car_dict.popitem()
#     print(car_dict)
#     car_dict[11] = 1 # możliwe jest użycie w jednym słowniku kluczy o dwóch różnych typach (np. int i string)
#     print(car_dict)
# task10()
# #zadanie 11
# def task11():
#     students = {
#         124445: {
#             "imie": "Filip",
#             "nazwisko": "Pezacki",
#             "oceny": [5, 4, 5]
#         },
#         124446: {
#             "imie": "Anna",
#             "nazwisko": "Kowalska",
#             "oceny": [4, 5, 5, 5]
#         },
#         124447: {
#             "imie": "Piotr",
#             "nazwisko": "Nowak",
#             "oceny": [3, 4, 3, 2]
#         }
#     }
#     for index, dane in students.items():
#         srednia = sum(dane["oceny"]) / len(dane["oceny"]) #Liczę średnią ocen dla danego studenta
#         print(f"Index: {index}, Imię: {dane['imie']}, Nazwisko: {dane['nazwisko']}, Średnia: {srednia}") #Wypisuję dane studenta i średnią ocen
# task11()
# #zadanie 12 -pytesty
# Zadanie 3 – zwraca elementy list3_1, które nie występują w list3_2
def unique_elements(list1, list2):
    unique = [element for element in list1 if element not in list2] #Tworzymy nową listę zawierającą tylko te elementy z list1, które nie znajdują się w list2
    return unique


# Zadanie 4 – zwraca liczby nieparzyste i najmniejszą z nich
def odd_numbers_and_min(lst):
    odd = [x for x in lst if x % 2 != 0] #Filtrujemy listę, pozostawiając tylko liczby nieparzyste
    odd.sort() #Sortujemy listę liczb nieparzystych, aby łatwo znaleźć najmniejszą
    smallest = odd[0] if odd else None #Pobieramy najmniejszą liczbę nieparzystą lub None, jeśli lista jest pusta
    return odd, smallest #Zwracamy listę liczb nieparzystych i najmniejszą liczbę

def main():
    pass