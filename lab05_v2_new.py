#
# input_string = "2,5"
# #version 1
# try:
#     # próba wykonania dzielenia liczby 3 przez 0 – operacja ta zawsze generuje ZeroDivisionError
#     some_number: float = 3 / 0
#     print(f"This number is: {some_number}")
# except (ValueError, UnicodeError) as ex1:
#     # ten blok obsługuje błędy konwersji tekstu na liczbę i problemy z Unicode – tu się nie wykona
#     print("Value/Unicode error!")
#     print(ex1)
# except ZeroDivisionError as ex:
#     # ten blok złapie wyjątek dzielenia przez zero, czyli sytuację, która wystąpi powyżej
#     print("ZeroDivisionError caught:", ex)
# except Exception as ex:
#     # ogólny blok na wszelkie inne wyjątki
#     print("Unknown error:", ex)
#
# #version 2
# try:
#     # próba zamiany napisu „2,5” na liczbę zmiennoprzecinkową – przecinek powoduje ValueError
#     some_number: float = float(input_string)
#     print(f"This number is: {some_number}")
# except (ValueError, UnicodeError) as ex1:
#     # wyjątek ValueError pojawi się, bo Python oczekuje kropki zamiast przecinka
#     print("Value/Unicode error!")
#     print(ex1)
#
# #version 3
# try:
#     input_string = "2.5"  # zmieniamy napis na poprawny zapis liczby
#     some_number: float = float(input_string)  # operacja udana – brak wyjątku
#     print("Correct number:", some_number)
# except Exception as ex:
#     print("Unexpected:", ex)


# #task 2
# x = -1  #ustawiamy wartość ujemną, która wywoła wyjątki
#
# #first
# try:
#     if x < 0:
#         raise Exception("liczba mniejsza niż 0") #celowo wywołuję ogólny wyjątek
# except Exception as ex:
#     print("Wyjątek - exception :", ex) #tu program ląduje po wyjątku i wyświetla komunikat
#
# #second
# try:
#     if x < 0:
#         raise ValueError("liczba poniżej 0")  #tym razem zgłaszam konkretny błąd typu ValueError
# except ValueError as ex:
#     print("Błąd - ValueError:", ex) #w przypadku wychwycenia konkretnego błędu wyświetlany jest error

# #task 3
# try:
#     value = input("Podaj liczbę: ") #prosimy użytkownika o podanie liczby
#     result = 10 / float(value) #zmieniamy wpisaną wartość na liczbę zmiennoprzecinkową, wpisanie "abc" = wywołuje ValueError
# except ValueError as Bad_type: #wyjątek ValueError wystąpi, gdy nie da się przekonwertować tekstu na liczbę
#     print("zły format liczby", Bad_type)
# except ZeroDivisionError as Bad_division: #wyjątek ZeroDivisionError wystąpi, gdy użytkownik wpisze "0"
#     print("Dzielenie przez 0: błąd -", Bad_division)
# else: #blok else wykona się tylko wtedy, gdy w bloku try nie wystąpi żaden błąd
#     print("Wynik dzielenia to: ", result)
# finally:
#     print("Koniec") #końcowy komunikat informujący o zakończeniu działania programu
#     #blok finally wykona się ZAWSZE, niezależnie od błędu

# #task 4
# import os
# def file_open(path : str, mode : str):
#     try:
#         with open(path, "r") as f: #próba otwarcia pliku
#             print(f.read()) #jeśli plik istnieje – wypisujemy jego zawartość
#     except FileNotFoundError as er:  #wyjątek występuje, gdy plik nie istnieje
#         print("plik nie istnieje.", er)
#
# def file_write(path : str, text : str, mode : str):
#     try:
#         with open(path, "w") as f: #próba otwarcia pliku w trybie 'w' (zapis – nadpisuje)
#             f.write(text) #zapis tekstu do pliku
#     except FileNotFoundError as er:
#         print("plik nie nie istnieje.", er)
#         file = open(path, "w")
#         file.close()
#         file = open(path, mode)
#     return file
#
# f = open("C:\Users\HAHHAHAHAHAHAH\Desktop\skryptowe jezyki programownaia\code\sem3\plik.txt", "r")
# print(f.read()) #odczyt całego pliku do końca
# f = open("plik.txt", "r")
# print(f.readline()) #odczyt jednej linii
# f = open("plik.txt", "r")
# print(f.read(10)) #odczyt pierwszych 10 znaków
# f = open("thefile.txt", "r")
#
# for x in f:
#         print(x)  # odczyt w pętli
# f = open("plik.txt", "r")
#
# list = f.readlines()  # wszystkie linie do listy
# list = f.realines(10)  # 10 pierwszych do listy
#
#
# f.close()  # otwarte pliki należy zamykać
#
# def task5():
#     # tryb w - zapis, Jeśli plik istnieje to zostaje całkowite nadpisany, jeśli nie istnieje plik zostaje stworzony
#     try:
#         f = open("test_w.txt", "w")
#         f.write("zapis w trybie w\n")
#         f.close()
#         print("w działa")
#     except Exception as e:
#         print("w błąd:", e)
#
#     # tryb a – Dopisywanie na koniec pliku, jeśli istnieje nic nie jest kasowane, natomiast w innym przypadku tworzy plik
#     try:
#         f = open("test_a.txt", "a")
#         f.write("dopisek z a\n")
#         f.close()
#         print("a działa")
#     except Exception as e:
#         print("a błąd:", e)
#
#     # tryb x – Tylko tworzy nowy plik (jesli istnieje, to błąd)
#     try:
#         f = open("test_x.txt", "x")
#         f.write("plik z x\n")
#         f.close()
#         print("x działa")
#     except Exception as e:
#         print("x błąd:", e)
# if __name__ == "__main__":

import os
def task6():
    # funkcja wypisująca zawartość katalogu
    def directory_tree(path: str,depth:int =0) -> None:
        try:
            entries = os.listdir(path)  # pobranie listy plików i folderów
        except FileNotFoundError:
            print("Podany katalog nie istnieje.")
        else:
            print("Wszystko poszło pomyślnie.")
        if len(entries) == 0:
            return
        for entry in entries:
            # drukujemy element ze stosownym wcięciem
            print("  " * depth + "|-- " + entry)
            # pełna ścieżka elementu
            full_path = os.path.join(path, entry)
            # sprawdzamy, czy element jest folderem
            if os.path.isdir(full_path):
                # jeśli tak → schodzimy głębiej
                directory_tree(full_path, depth + 1)
            # jeśli to plik → nic nie robimy (rekurencja niepotrzebna)
    # wywołanie funkcji z przykładową ścieżką
    directory_tree("C:\\Users\\HAHHAHAHAHAHAH\\Desktop\\skryptowe jezyki programownaia\\code\\sem3\\test")
if __name__ == "__main__":
    task6()
