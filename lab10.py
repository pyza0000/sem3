import matplotlib.pyplot as plt  # import biblioteki matplotlib do rysowania wykresów
import numpy as np  # import biblioteki numpy do obliczeń numerycznych

# task 1
def task1():  # definicja funkcji do zadania 1
    x = np.linspace(-np.pi, np.pi, 100)  # generowanie 100 punktów od -pi do pi
    y1 = np.sin(x)  # obliczenie wartości sin(x)
    y2 = 2 * np.cos(x)  # obliczenie wartości 2*cos(x)
    plt.plot(x, y1, label="sin(x)")  # rysowanie wykresu sin(x)
    plt.plot(x, y2, label="2cos(x)")  # rysowanie wykresu 2cos(x)
    plt.title("Wykres sin(x) oraz 2cos(x)")  # tytuł wykresu
    plt.xlabel("x")  # opis osi X
    plt.ylabel("wartość funkcji")  # opis osi Y
    plt.legend()  # wyświetlenie legendy
    plt.grid(True)  # włączenie siatki
    plt.show()  # wyświetlenie wykresu

# task 2
def task2():  # definicja funkcji do zadania 2
    labels = 'Frogs', 'Cats', 'Dogs', 'Birds'  # etykiety wykresu kołowego
    sizes = [20, 25, 40, 15]  # wartości procentowe dla kategorii
    explode = (0, 0.1, 0, 0)  # odsunięcie jednego fragmentu wykresu
    fig1, ax1 = plt.subplots()  # utworzenie figury i osi
    ax1.pie(  # rysowanie wykresu kołowego
        sizes,  # dane do wykresu
        explode=explode,  # efekt odsunięcia
        labels=labels,  # etykiety
        autopct='%1.1f%%',  # format procentów
        shadow=True,  # cień wykresu
        startangle=90)  # kąt startowy wykresu
    ax1.set_title("Wykres- zakres ludnosci zwierzat")  # tytuł wykresu
    ax1.legend(labels, title="Zwierze", loc="center left", bbox_to_anchor=(1.0, 0.5))  # legenda
    plt.show()  # wyświetlenie wykresu

# task 3
def task3():  # definicja funkcji do zadania 3
    fig, ax = plt.subplots()  # utworzenie figury i osi
    fruits = ['apple', 'blueberry', 'cherry', 'orange', 'strawberry']  # nazwy owoców
    counts = [40, 100, 30, 55, 75]  # liczba spożyć
    bar_labels = ['green', 'blue', '_red', 'orange', 'red']  # etykiety legendy
    bar_colors = ['green', 'blue', 'red', 'orange', 'red']  # kolory słupków
    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)  # wykres słupkowy
    ax.set_ylabel('ilość spożytkowania')  # opis osi Y
    ax.set_title('Najchętniej spożywane owoce')  # tytuł wykresu
    ax.legend(title='nazwa owoca')  # legenda
    plt.show()  # wyświetlenie wykresu

# task 4
def task4():  # definicja funkcji do zadania 4
    np.random.seed(4)  # ustawienie ziarna losowości
    x = np.arange(10)  # wartości osi X od 0 do 9
    format1 = np.random.randint(0, 100, size=10)  # losowe dane 1
    format2 = np.random.randint(0, 100, size=10)  # losowe dane 2
    format3 = np.random.randint(0, 100, size=10)  # losowe dane 3
    plt.plot(x, format1, "Dg-", label="zielone diamenty")  # wykres z diamentami
    plt.plot(x, format2, "*y-.", label="żółte gwiazdki")  # wykres z gwiazdkami
    plt.plot(x, format3, "pm--", label="fioletowe pięciokąty")  # wykres z pięciokątami
    plt.title("liczby - różne formatowania linii")  # tytuł wykresu
    plt.xlabel("X-<0-9>")  # opis osi X
    plt.ylabel("Y-losowe liczby całkowite")  # opis osi Y
    plt.legend()  # legenda
    plt.grid(True)  # siatka
    plt.xticks(x)  # ustawienie znaczników osi X
    plt.show()  # wyświetlenie wykresu

# task 5
def task5():  # definicja funkcji do zadania 5
    np.random.seed(7)  # ustawienie ziarna losowości
    table = np.random.randint(0, 10, 100)  # losowa tablica liczb
    quantity = np.arange(10)  # zakres liczb 0–9
    counts = np.bincount(table, minlength=10)  # zliczanie wystąpień
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))  # dwa wykresy obok siebie
    ax[0].bar(quantity, counts)  # wykres słupkowy
    ax[0].set_title("Liczba powtórzeń ")  # tytuł wykresu
    ax[0].set_xlabel("Liczba")  # opis osi X
    ax[0].set_ylabel("występowanie")  # opis osi Y
    ax[0].set_xticks(quantity)  # znaczniki osi X
    ax[1].hist(table, bins=np.arange(-0.5, 10.5, 1), rwidth=0.9)  # histogram
    ax[1].set_title("Histogram ")  # tytuł histogramu
    ax[1].set_xlabel("Liczba")  # opis osi X
    ax[1].set_ylabel("występowanie")  # opis osi Y
    ax[1].set_xticks(quantity)  # znaczniki osi X
    plt.show()  # wyświetlenie wykresów

# task 6
def task6():  # definicja funkcji do zadania 6
    x = np.linspace(-np.pi, np.pi, 100)  # zakres argumentów
    y = np.sin(x)  # wartości sin(x)
    plt.figure()  # nowa figura
    plt.plot(x, y, label='sin(x)')  # wykres funkcji
    plt.title("legenda loc - napis")  # tytuł wykresu
    plt.xlabel("liczby")  # opis osi X
    plt.ylabel("wartości ")  # opis osi Y
    plt.legend(loc="center left")  # legenda jako napis
    plt.show()  # wyświetlenie wykresu

    plt.figure()  # nowa figura
    plt.plot(x, y, label='sin(x)')  # wykres funkcji
    plt.title("legenda loc - liczba")  # tytuł wykresu
    plt.xlabel("liczby")  # opis osi X
    plt.ylabel("wartości ")  # opis osi Y
    plt.legend(loc=4)  # legenda jako liczba
    plt.show()  # wyświetlenie wykresu

# task 7
def task7():  # definicja funkcji do zadania 7
    t = np.linspace(0, 2*np.pi, 100)  # zakres argumentów
    s1 = np.sin(t)  # sin(x)
    c1 = np.cos(t)  # cos(x)
    t1 = np.tan(t)  # tan(x)
    s2 = np.sin(2*t)  # sin(2x)
    plt.figure(figsize=(10, 7))  # rozmiar figury
    plt.subplot(2, 2, 1)  # pierwszy wykres
    plt.plot(t, s1, color='red')  # wykres sin(x)
    plt.title("Wykres sin(x)")  # tytuł
    plt.grid()  # siatka
    plt.subplot(2, 2, 2)  # drugi wykres
    plt.plot(t, c1, 'g')  # wykres cos(x)
    plt.title("Funkcja cos(x)")  # tytuł
    plt.grid()  # siatka
    plt.subplot(2, 2, 3)  # trzeci wykres
    plt.plot(t, t1)  # wykres tan(x)
    plt.ylim(-5, 5)  # ograniczenie osi Y
    plt.title("Wykres tan(x)")  # tytuł
    plt.grid()  # siatka
    plt.subplot(2, 2, 4)  # czwarty wykres
    plt.plot(t, s2, 'b--')  # wykres sin(2x)
    plt.title("Funkcja sin(2x)")  # tytuł
    plt.grid()  # siatka
    plt.suptitle("rożne funkcje trygonometryczne")  # tytuł całej figury
    plt.tight_layout()  # dopasowanie układu
    plt.show()  # wyświetlenie wykresów

# task 8
def task8():  # definicja funkcji do zadania 8
    data = np.genfromtxt("oceny.csv", delimiter="\t", skip_header=1)  # wczytanie danych z pliku
    labs = data[:, :5]  # wybór kolumn z ocenami laboratoriów
    labs_flat = labs.flatten()  # spłaszczenie tablicy do jednego wymiaru
    labs_flat = labs_flat[~np.isnan(labs_flat)]  # usunięcie wartości NaN
    values, counts = np.unique(labs_flat, return_counts=True)  # unikalne oceny i ich liczność
    plt.figure(figsize=(7, 7))  # rozmiar figury
    plt.pie(  # wykres kołowy
        counts,  # liczności ocen
        labels=values,  # etykiety ocen
        autopct="%1.1f%%",  # format procentów
        startangle=90  # kąt startowy
    )
    plt.title("Rozkład ocen z laboratoriów – cała grupa")  # tytuł wykresu
    plt.savefig("lab10_task8.png", dpi=300)  # zapis wykresu do pliku
    plt.show()  # wyświetlenie wykresu

if __name__ == "__main__":  # sprawdzenie czy plik jest uruchamiany bezpośrednio
    task8()  # wywołanie zadania 8
