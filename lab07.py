import re
import os
import typing

def task1():
    f = open("inwokacja.txt","r")
    content = f.read()
    f.close()
    lines = content.strip().split("\n")
    print("Liczba wierszy:", len(lines))
    total_chars = 0
    total_words = 0
    f = open("inwokacja.txt", "r")
    for i, line in enumerate(f):
        stripped = line.strip()
        chars = len(stripped)
        words = len(stripped.split())
        print(f"Wiersz {i + 1}: znaki = {chars}, wyrazy = {words}")
        total_chars += chars
        total_words += words
    f.close()
    print("Suma znaków:", total_chars)
    print("Suma wyrazów:", total_words)


def task2():
    f = open("inwokacja.txt","r")
    content = f.read()
    print(f"nowe linie {content.count("\n")}")
    print(f"spacje {content.count(" ")}")
    print(f"tabulatory {content.count("\t")}")
    f.close()

def task3():
    f = open("inwokacja.txt", "r")
    content = f.read()
    f.close()
    text_replaced = content.replace("...", "<ELLIPSIS>")
    text_replaced = content.replace(".", "...")
    print(text_replaced)

def task4():
    list = ["Filip","Grzegorz","Daniel","Bartek","Anastazja"]
    for n in list:
        if re.fullmatch(r"[A-Z][a-z]*a",n):
            print(n)

def task5():
    import re
    with open("numery.txt", "r") as t5:
        lines = t5.readlines()
    pattern = re.compile(r"^(?:\+48|0048)\s*\d+")
    for line in lines:
        line = line.strip()
        if pattern.match(line):
            print(line)

def task6():
    import re
    with open("numery.txt", "r") as t6:
        numbers = [n.strip() for n in t6.readlines()]
    regex_format_1 = r"^\+48\d{9}$"
    regex_format_2 = r"^0048\d{9}$"
    regex_format_3 = r"^\+48\s(\d{3}\s){2}\d{3}$"
    count_format_1 = 0
    count_format_2 = 0
    count_format_3 = 0
    for numer in numbers:
        number_cl = numer.strip()
        if re.match(regex_format_1, number_cl):
            count_format_1 += 1
        elif re.match(regex_format_2, number_cl):
            count_format_2 += 1
        elif re.match(regex_format_3, number_cl):
            count_format_3 += 1
    print(f"Liczba numerów w formacie '{regex_format_1}' (+48... bez spacji): {count_format_1}")
    print(f"Liczba numerów w formacie '{regex_format_2}' (0048... bez spacji): {count_format_2}")
    print(f"Liczba numerów w formacie '{regex_format_3}' (+48 XXX XXX XXX ze spacjami): {count_format_3}")
def task7():
    import re
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    emails = ["pyza171@gmail.com", "filpez000@pbs.edu.pl", "koduje.tylko.w.nocy@gmail.com"]
    for x in emails:
        if pattern.match(x):
            print(x, "prawidłowy")
        else:
            print(x, "niepoprawny")
def task8():
    import re
    pattern = re.compile(r"^(0[1-9]|[12][0-9]|3[01])([-\/])(0[1-9]|1[0-2])\2(\d{4})$")
    date = input("Podaj datę (dd-mm-yyyy lub dd/mm/yyyy): ")
    m = pattern.match(date)
    if m:
        day = m.group(1)
        month = m.group(3)
        year = m.group(4)
        months = {
            "01": "styczeń",
            "02": "luty",
            "03": "marzec",
            "04": "kwiecień",
            "05": "maj",
            "06": "czerwiec",
            "07": "lipiec",
            "08": "sierpień",
            "09": "wrzesień",
            "10": "październik",
            "11": "listopad",
            "12": "grudzień"
        }
        print(f"Data poprawna, miesiąc: {months[month]}")
    else:
        print("Niepoprawny format daty")
def task9():
    import os
    import re
    directory = "test/"
    pattern = re.compile(r".+\.txt$")
    for file in os.listdir(directory):
        if pattern.match(file):
            print(file)
def task10():
    import re
    words = ["pbs", "student", "atm", "brak", "snu", "projekt", "imprezy", "wykłady", "stm", "index"]
    end_xy = []
    for w in words:
        if re.match(r".*[xy]$", w):
            end_xy.append(w)
    three_a = []
    for w in words:
        if re.match(r"^a..$", w):
            three_a.append(w)
    vowel = []
    for w in words:
        if re.match(r"^[aeiou].*", w):
            vowel.append(w)
    print("Koniec x/y:", end_xy)
    print("Trzyznakowe od a:", three_a)
    print("Samogłoski:", vowel)
def task11():
    pass
if __name__ == '__main__':
    task8()
    pass
