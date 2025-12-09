import re
def task1():
    text = "aaaa"
    for pattern in ["a+", "a+?", "a*", "a*?", "a?", "a??"]:
        print(pattern, re.findall(pattern, text))
def task2():
    text = open("inwokacja.txt", encoding="utf-8").read()
    resultA = re.findall(r"\w+(?=!)", text)
    print(resultA)
    resultB = re.findall(r"\w*[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+\w*", text)
    print(resultB)
    resultC = re.findall(r"\b(cię|ci)\b", text, flags=re.I)
    print(len(resultC))
def task3():
    text = open("adresy.txt", encoding="utf-8").read()
    ulice = re.findall(r"([A-Za-zĄĆĘŁŃÓŚŹŻąęćłńóśźż\. ]+?) \d", text)
    kody = re.findall(r"\b\d{2}-\d{3}\b", text)
    mieszkania = re.findall(r"\d+[A-Za-z]?/\d+[A-Za-z]?", text)
    print(ulice)
    print(kody)
    print(mieszkania)
def task4():
    adres = "Al. prof. S. Kaliskiego 7 85-796 Bydgoszcz"
    result = re.search(r"([A-Za-zĄĆĘŁŃÓŚŹŻąęćłńóśźż\. ]+?) \d{1,3}", adres)
    print(result.group(1))
def task5():
    result = re.match("[a-z]{3}", "Ala ma kota a kot ma Ale", flags=re.I)
    if result:
        print(result.group())
    else:
        print("Brak dopasowania")
def task6():
    def check_strength(password):
        strong = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{10,}$"
        medium = r"^(?=.*[A-Z])(?=.*[a-z]).{8,}$"
        weak = r"^.{6,}$"
        if re.match(strong, password):
            return "mocne"
        elif re.match(medium, password):
            return "średnie"
        elif re.match(weak, password):
            return "słabe"
        else:
            return "niepoprawne"
    passwords = ["Kotek", "Haslo12", "MocneHaslo12@", "siema1234"]
    for p in passwords:
        print(p, " → ", check_strength(p))
def task7():
    text = "BYdgoszcz jest w POlsce, a moja koleżanka ma na imię ANNa. Studiuję w poliTEchnika w mieście IT."
    text_corrected = re.sub(r"\b([A-Z])([A-Z])([a-z]+)\b", lambda x: x.group(1) + x.group(2).lower() + x.group(3), text)
    two_letter = re.findall(r"\b[A-Z]{2}\b", text_corrected)
    for word in two_letter:
        decision = input(f"Czy poprawić '{word}' na '{word.capitalize()}'? (t/n): ")
        if decision.lower() == "t":
            text_corrected = text_corrected.replace(word, word.capitalize())
    print(text_corrected)
if __name__ == "__main__":
    task2()