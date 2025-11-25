import re
import os
import typing

def task1():
    f = open("C:/Users/pyza1/Downloads/inwokacja.txt","r")
    content = f.read()
    f.close()
    lines = content.strip().split("\n")
    print("Liczba wierszy:", len(lines))
    total_chars = 0
    total_words = 0
    f = open("C:/Users/pyza1/Downloads/inwokacja.txt", "r")
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
    f = open("C:/Users/pyza1/Downloads/inwokacja.txt","r")
    content = f.read()
    print(f"nowe linie {content.count("\n")}")
    print(f"spacje {content.count(" ")}")
    print(f"tabulatory {content.count("\t")}")
    f.close()

def task3():
    f = open("C:/Users/pyza1/Downloads/inwokacja.txt", "r")
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
    f = open

if __name__ == '__main__':

    pass
