from typing import List
class Student:
    def __init__ (self):
        self.name = ""
        self.last_name = ""
        self.marks = []
    def give_name(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name
    def give_mark(self, mark: int) -> None:
        self.marks.append(mark)
    def get_marks(self) -> List[int]:
        return self.marks
    def say_hello(self) -> None:
        print("Hello! I'm " + self.name + " " + self.last_name)

s = Student()
s.give_name("Jane", "Doe")
s.give_mark(5) # wywołanie sposób 1
Student.give_mark(s, 3)  # wywołanie sposób 2
print(s.get_marks())
s.say_hello()