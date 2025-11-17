from typing import List

class Student:
    quantity = 0
    index = 124445
    def __init__ (self):
        self.name = ""
        self.last_name = ""
        self.marks = []
        Student.quantity += 1
        Student.index += 1
        self.index = Student.index
    def give_name(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name
    def give_mark(self, mark: int) -> None:
        self.marks.append(mark)
    def get_marks(self) -> List[int]:
        return self.marks
    def say_hello(self) -> None:
        if self.isnamed():
            print("Hello! I'm " + self.name + " " + self.last_name + "my index is : " + str(self.index))
        else:
            print("Sorry, I don't have a name")
    def getavg(self) -> float:
        return sum(self.marks) / len(self.marks)
    def giveindex(self,idx: int) -> None:
        self.index = idx
    def isnamed(self):
        if self.name != "" and self.last_name != "":
            return True
        return False
    def __eq__(self, o: object) -> bool:
        return self.getavg()==o.getavg()
    def __ne__(self, o: object) -> bool:
        return self.getavg()!=o.getavg()
    def __lt__(self, o: object) -> bool:
        return self.getavg()<o.getavg()
    def __gt__(self, o: object) -> bool:
        return self.getavg()>o.getavg()
    def __le__(self, o: object) -> bool:
        return self.getavg()<=o.getavg()
    def __ge__(self, o: object) -> bool:
        return self.getavg()>=o.getavg()
    def __repr__(self) -> str:
        return f"Student('{self.name}', '{self.last_name}', index={self.index}, marks={self.marks})"
    def __str__(self) -> str:
        avg = self.getavg()
        return f"Student: {self.name} {self.last_name}, index: {self.index}, avg: {avg:.2f}"
def task1():
    s1 = Student()
    s1.give_name("Jane", "Doe")
    s1.give_mark(5)
    s1.give_mark(4)
    s2 = Student()
    s2.give_name("Mateusz", "Kowalski")
    s2.give_mark(3)
    s2.give_mark(4)

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
# class Item:
#     def get_sound(self) -> None:
#         print("item's sound")
# class Element:
#     def get_sound(self) -> None:
#         print("element's sound")
# # class Thing(Element, Item):
# #     def say_hello(self)  -> None:
# #         print("hello")
# class Thing(Item,Element): #zmieniona kolejność
#     def say_hello(self)  -> None:
#         print("hello")
# def test_sound():
#     i  = Item()
#     e = Element()
#     t = Thing()
#
#     t.get_sound()
#     e.get_sound()
#     i.get_sound()

#zadanie 9
# class Vehicle():
#     def __init__(self, owner:str):
#         print("Initializing Vehicle")
#         self.owner = owner
#     def get_sound(self):
#         print("Vehicle's brum brum")
#     def get_owner(self):
#         return ""
# class Tank(Vehicle):
#     def __init__(self, owner:str, type:str):
#         super().__init__(owner)
#         print("Initializing Tank")
#         self.type = type
def main():
    task1()
if __name__ == "__main__":
    main()
