from typing import List
# class Student:
#     def __init__ (self):
#         self.name = ""
#         self.last_name = ""
#         self.marks = []
#     def give_name(self, name: str, last_name: str) -> None:
#         self.name = name
#         self.last_name = last_name
#     def give_mark(self, mark: int) -> None:
#         self.marks.append(mark)
#     def get_marks(self) -> List[int]:
#         return self.marks
#     def say_hello(self) -> None:
#         print("Hello! I'm " + self.name + " " + self.last_name + "my index is : "
#               + str(self.index))
#     def getavg(self) -> float:
#         return (sum(self.marks) / len(self.marks))
#     def giveindex(self,idx: str) -> None:
#         self.index = idx
#
# s = Student()
# s.give_name("Jane", "Doe")
# s.give_mark(5) # wywołanie sposób 1
# Student.give_mark(s, 3)  # wywołanie sposób 2
# print(s.get_marks())
# s.giveindex("77")
# s.say_hello()
# print(f"średnia ocen {s.getavg()}")

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
#     v.get_owner() #klasa vehicle nie posiada metody get_owner
#     c.get_owner()
# vehicle_test()

#zadanie 3____________________________________________________
class Student:
    quantity = 0
    def __init__ (self):
        self.name = ""
        self.last_name = ""
        self.marks = []
        Student.quantity += 1
