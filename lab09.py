import numpy as np #import biblioteki numpy
#
def replace_zeros(A, x): #funkcja zamienia zera na podaną wartość
    array1 = np.array(A) #konwersja listy na tablicę numpy
    array1[array1 == 0] = x #zamiana zer na x
    return array1.tolist() #zwrócenie wyniku jako listy

def task1(): #funkcja testująca zadanie 1
    A = [[0, 1, 0], [2, 0, 3]] #przykładowa macierz
    print(replace_zeros(A, 3)) #wywołanie funkcji

# def medianize(A): #funkcja odejmująca średnią od elementów
#     array2 = np.array(A, dtype=float) #konwersja na float
#     mean = array2.mean() #obliczenie średniej
#     return array2 - mean #zwrócenie zmodyfikowanej tablicy
#
# def task2(): #funkcja testująca zadanie 2
#     A = [1,3,4,5,6,7,2,3,5,10] #przykładowe dane
#     print(medianize(A)) #wypisanie wyniku

# def max_values(A): #funkcja obliczająca maksima
#     max_result_global = np.max(A) #maksimum globalne
#     max_result_column = A.max(axis=0) #maksima w kolumnach
#     max_result_row = A.max(axis=1) #maksima w wierszach
#     print("macierz ogolnie:\n ", A) #wypisanie macierzy
#     print("maksymalna wartosc globalna: ", max_result_global) #wypisanie maksimum
#     print("maksymalne wartosci w kolumnach: ", max_result_column) #kolumny
#     print("maksymalne wartosci w wierszach: ", max_result_row) #wiersze
#
# def task3(): #funkcja testująca zadanie 3
#     matrix = np.random.randint(100,size=(3,3)) #losowa macierz 3x3
#     max_values(matrix) #wywołanie funkcji

# def task4(): #funkcja testująca reshape
#     A = np.arange(42) #utworzenie tablicy od 0 do 41
#     print(A) #wypisanie tablicy
#     A1 = A.reshape(-1,6) #reshape z -1 jako pierwszy parametr
#     print("\n",A1) #wypisanie macierzy
#     A2 = A.reshape(7,-1) #reshape z -1 jako drugi parametr
#     print("\n",A2) #wypisanie macierzy

# def task5(): #zadanie z plikiem csv
#     data = np.genfromtxt("oceny.csv", delimiter="\t", skip_header=1) #wczytanie danych z pliku
#     labs = data[:, :5] #wydzielenie kolumn laboratoriów
#     exam = data[:, 5] #wydzielenie kolumny egzaminu
#
#     print("Najniższa ocena z laboratoriów:") #opis
#     for i in range(len(labs)): #iteracja po studentach
#         print("Student", i + 1, ":", np.min(labs[i])) #minimum z laboratoriów
#
#     average_exam = np.mean(exam) #średnia ocen z egzaminu
#     print("Średnia ocen z egzaminu:", average_exam) #wypisanie średniej
#
#     countTwo = 0 #licznik ocen 2
#     for grade in exam: #iteracja po ocenach
#         if grade == 2: #sprawdzenie oceny
#             countTwo += 1 #zwiększenie licznika
#     print("Liczba ocen 2 z egzaminu:", countTwo) #wypisanie wyniku
#
#     all5 = False #flaga samych piątek
#     for row in labs: #iteracja po wierszach
#         if np.all(row == 5): #sprawdzenie czy same piątki
#             all5 = True #ustawienie flagi
#     print("Czy jest student z samymi 5 z laboratoriów:", all5) #wynik
#
#     twoInLab2Lab3 = False #flaga dwójek
#     for row in labs: #iteracja po wierszach
#         if row[1] == 2 and row[2] == 2: #sprawdzenie LAB2 i LAB3
#             twoInLab2Lab3 = True #ustawienie flagi
#     print("Czy jest student z 2 z LAB2 i LAB3:", twoInLab2Lab3) #wynik
#
#     betterExamGrade = 0 #licznik studentów
#     for i in range(len(labs)): #iteracja po studentach
#         lab_mean = np.mean(labs[i]) #średnia z laboratoriów
#         if exam[i] > lab_mean: #porównanie z egzaminem
#             betterExamGrade += 1 #zwiększenie licznika
#     print("Liczba studentów z wyższym egzaminem niż średnia z labów:", betterExamGrade) #wynik
#
#     bestOfAll = 0 #maksymalna liczba piątek
#     for row in labs: #iteracja po studentach
#         five_count = 0 #licznik piątek
#         for grade in row: #iteracja po ocenach
#             if grade == 5: #sprawdzenie piątki
#                 five_count += 1 #zwiększenie licznika
#         if five_count > bestOfAll: #porównanie maksimum
#             bestOfAll = five_count #zapis maksimum
#     print("Największa liczba piątek jednego studenta:", bestOfAll) #wynik

# def task6(): #zadanie sortowania
#     table = np.random.randint(0,100,10) #losowa tablica
#     print("tablica - przed sortowaniem:", table) #wypisanie tablicy
#     tableUp = np.sort(table) #sortowanie rosnąco
#     print("tablica - posortowana rosnąco", tableUp) #wynik
#     tableDown = np.sort(table)[::-1] #sortowanie malejąco
#     print("tablica - posortowana malejąco", tableDown) #wynik

# def task7(): #zadanie średniej ważonej
#     table = np.random.randint(0, 10, (5, 5)) #losowa macierz
#     weight = [1,2,3,2,1] #wagi
#     for row in table: #iteracja po wierszach
#         total = 0 #suma ważona
#         total_weight = 0 #suma wag
#         for i in range(5): #iteracja po elementach
#             total += row[i] * weight[i] #dodanie iloczynu
#             total_weight += weight[i] #dodanie wagi
#         average = total / total_weight #obliczenie średniej
#         print(f"średnia: {average:.2f}") #wypisanie wyniku
#
# def task8(): #zadanie zliczania wystąpień
#     table = np.random.randint(0, 10, size=(10, 10)) #losowa macierz
#     print(table) #wypisanie macierzy
#     for i in range(10): #iteracja po wartościach
#         quantity = 0 #licznik
#         for row in table: #iteracja po wierszach
#             for element in row: #iteracja po elementach
#                 if element == i: #sprawdzenie wartości
#                     quantity += 1 #zwiększenie licznika
#         print("Liczba", i, "występuje", quantity, "razy") #wynik

# def task9(): #zadanie operatorów * i @
#     A = np.array([1,3,4]) #wektor A
#     B = np.array([2,5,6]) #wektor B
#     C = np.array([[7,8],[9,10]]) #macierz C
#     D = np.array([[10,11],[12,13]]) #macierz D
#     print("A*B \n",A*B) #mnożenie elementów
#     print("C@D \n",C@D) #mnożenie macierzy
#
# def task10(): #miejsce na testy pytest
#     pass #zadanie 10 realizowane w osobnym pliku testów

if __name__ == "__main__": #punkt startowy programu
    task9() #wywołanie wybranego zadania
