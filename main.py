# Zadanie 4

# 1. Próba otwarcia pliku do odczytu, który NIE istnieje
try:
    f = open("nie_ma_takiego_pliku.txt", "r")#otwieranie pliku w trybie r
    print(f.read())#próba czytania
    f.close()#zamknięcie pliku
except Exception as e:
    print("Błąd przy otwieraniu pliku w trybie r:", e)#wyjątek przy braku pliku


# 2. Próba otwarcia pliku do zapisu i zapisania danych
try:
    f = open("plik_testowy.txt", "w")#otwieranie pliku w trybie w
    f.write("Test zapisu")#zapisanie tekstu
    f.close()#zamknięcie
    print("Zapis działa")#sukces
except Exception as e:
    print("Błąd przy zapisie:", e)#wyjątek przy zapisie


# 3. Próba zapisu do pliku otwartego w trybie r (błąd zapisu)
try:
    f = open("plik_testowy_r.txt", "r")#otwarcie w trybie r
    f.write("Nie zapiszę tego")#próba zapisu → błąd
    f.close()#zamknięcie
except Exception as e:
    print("Błąd przy próbie zapisu w trybie r:", e)#wyjątek zapisu w trybie r
