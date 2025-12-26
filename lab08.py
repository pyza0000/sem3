import re #import biblioteki do wyrażeń regularnych

# Task 1
def task1(): #funkcja do zadania 1
    word = "alamakota" #tekst do testowania regexów
    print("a+  (zachłanny): ", re.findall("a+", word)) #dopasowanie jednego lub więcej a
    print("a+? (leniwy):    ", re.findall("a+?", word)) #dopasowanie leniwe a
    print("a* (zachłanny): ", re.findall("a*", word)) #dopasowanie zero lub więcej a
    print("a*? (leniwy):    ", re.findall("a*?", word)) #leniwe dopasowanie a
    print("a?  (zachłanny): ", re.findall("a?", word)) #dopasowanie jednego lub zera a
    print("a?? (leniwy):    ", re.findall("a??", word)) #leniwe dopasowanie jednego lub zera a

# Task 2
def task2(): #funkcja do zadania 2
    with open("inwokacja.txt", "r", encoding="utf-8") as file: #otwarcie pliku z tekstem
        textTask2 = file.read() #wczytanie zawartości pliku
    print("słowa, po których występuje !") #opis wyniku
    listA = re.findall(r"\w+(?=!)", textTask2) #wyszukanie słów przed !
    print(listA) #wyświetlenie wyniku
    print("słowa z polskimi znakami") #opis wyniku
    listB = re.findall(r"\w*[ąćęłńóśżźĄĆĘŁŃÓŚŻŹ]+\w*", textTask2) #wyszukanie słów z polskimi znakami
    print(listB) #wyświetlenie wyniku
    print(" wystąpienia słowa cię/ci") #opis wyniku
    listC = re.findall(r"\b(ci|cię)\b", textTask2, re.I) #wyszukanie słów ci lub cię
    print(len(listC)) #wyświetlenie ilości wystąpień

# Task 3
def task3(): #funkcja do zadania 3
    with open("adresy.txt", "r", encoding="utf-8") as file: #otwarcie pliku z adresami
        textTask3 = file.read() #wczytanie zawartości pliku
    print("ulice:") #opis wyniku
    street_result = re.findall(r"^[ \t]*([A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\.\- ]+?)\s+\d+", textTask3,re.M) #wyszukanie nazw ulic
    print(street_result) #wyświetlenie ulic
    print("kody pocztowe:") #opis wyniku
    post_code_result = re.findall(r"\d{2}-\d{3}", textTask3) #wyszukanie kodów pocztowych
    print(post_code_result) #wyświetlenie kodów
    print("numery mieszkania:") #opis wyniku
    flat_number_result = re.findall(r"\d+/\d+", textTask3) #wyszukanie numerów mieszkań
    print(flat_number_result) #wyświetlenie numerów mieszkań

# Task 4
def task4(): #funkcja do zadania 4
    address = "Al. prof. S. Kaliskiego 7 85-796 Bydgoszcz" #adres PBŚ
    result = re.search(r"^(.+?)\s+\d+", address) #wyszukanie samej nazwy ulicy
    if result: #sprawdzenie, czy znaleziono dopasowanie
        print(result.group(1)) #wyświetlenie nazwy ulicy bez numeru

# Task 5
def task5(): #funkcja do zadania 5
    textTask5 = "Ala ma kota a kot ma Ale" #tekst testowy
    result = re.match("[a-z]{3}", textTask5, re.I) #sprawdzenie 3 liter na początku tekstu
    if result: #jeśli znaleziono dopasowanie
        print("z flagą :", result.group()) #wyświetlenie dopasowania
    else: #jeśli brak dopasowania
        print("bez flagi") #informacja o braku dopasowania

# Task 6
def task6(): #funkcja do zadania 6
    password_list = ["12456", "student1234", "Student1234@", "Maciek1234"] #lista haseł
    for p in password_list: #pętla po hasłach
        if re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{10,}$", p): #warunek hasła silnego
            print(p, "silne") #wypisanie hasła silnego
        elif re.match(r"^(?=.*[A-Z])(?=.*[a-z]).{8,}$", p): #warunek hasła średniego
            print(p, "średnie") #wypisanie hasła średniego
        elif re.match(r"^.{6,}$", p): #warunek hasła słabego
            print(p, "słabe") #wypisanie hasła słabego
        else: #pozostałe przypadki
            print(p, "nieprawidłowe") #informacja o złym haśle

# Task 7
def task7(): #funkcja do zadania 7
    textTask7 = "BYdgoszcz is in POland and I study at poliTEchnika and IT" #tekst z błędami
    print("tekst przed:", textTask7) #przed poprawą

    def fix_word(m): #funkcja pomocnicza do re.sub
        w = m.group(0) #pobrane słowo
        bad = any(ch.isupper() for ch in w[1:]) #czy są wielkie litery po pierwszej
        if not bad: #jeśli nie ma błędu
            return w #zostawiamy słowo
        if len(w) == 2: #jeśli słowo ma 2 litery
            answ = input("Naprawić " + w + " w " + w.capitalize() + "? (y/n): ") #pytanie
            if answ == "y": #zgoda
                return w.capitalize() #poprawiamy
            return w #bez zmian
        return w.capitalize() #dłuższe poprawiamy automatycznie

    textTask7 = re.sub(r"\b[A-Za-z]+\b", fix_word, textTask7) #wyszukanie słów i poprawa przez sub
    print("tekst po:", textTask7) #po poprawie

if __name__ == "__main__": #sprawdzenie czy plik jest uruchamiany bezpośrednio
    task4() #wywołanie zadania
