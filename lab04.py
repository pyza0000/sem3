from typing import List
#
# class Student:
#     quantity = 0
#     index = 124445
#     def __init__ (self):
#         self.name = ""
#         self.last_name = ""
#         self.marks = []
#         Student.quantity += 1
#         Student.index += 1
#     def give_name(self, name: str, last_name: str) -> None:
#         self.name = name
#         self.last_name = last_name
#     def give_mark(self, mark: int) -> None:
#         self.marks.append(mark)
#     def get_marks(self) -> List[int]:
#         return self.marks
#     def say_hello(self) -> None:
#         if self.isnamed():
#             print("Hello! I'm " + self.name + " " + self.last_name + "my index is : " + str(self.index))
#         else:
#             print("Sorry, I don't have a name")
#     def getavg(self) -> float:
#         return (sum(self.marks) / len(self.marks))
#     def giveindex(self,idx: int) -> None:
#         self.index = idx
#     def isnamed(self):
#         if self.name != "" and self.last_name != "":
#             return True
#         return False
# def task1():
#     s1 = Student()
#     s2 = Student()
#     s3 = Student()
#     s1.say_hello()   #nie podano danych
#
#     s2.give_name("John", "Smith")
#     s2.say_hello() # podano dane
#
#     print(s3.isnamed()) #bezpośrednie wywołanie

#zadanie 2 --------------------------------------------------------------------------------------------S
# class Vehicle:
#     def get_sound(self) -> None:
#         print("vehicle's brum brum")
#     def get_owner(self) -> None:
#         return ""
# class Car(Vehicle):
#     def __init__ (self, owner: str, table: str):
#         self.owner = owner
#         self.table = table
#     def get_sound(self) -> None:
#         print("car's brum brum")
#     def get_owner(self) -> str:
#         return self.owner
# def vehicle_test():
#     v = Vehicle()
#     c = Car("Filip","PWA")
#
#     v.get_sound()
#     c.get_sound()
#     v.get_owner() #błąd wynikał z klasy vehicle, która nie posiadała metody get_owner
#     c.get_owner()
# vehicle_test()

#zadanie 5 ______________________________________________
class Item:
    def get_sound(self) -> None:
        print("item's sound")
class Element:
    def get_sound(self) -> None:
        print("element's sound")
class Thing(Element, Item):
    def say_hello(self)  -> None:
        print("hello")
def test_sound():
    i  = Item()
    e = Element()
    t = Thing()
    t.say_hello()
    e.get_sound()
    i.get_sound()
def main():
    test_sound()
    # task1()
if __name__ == "__main__":
    main()
