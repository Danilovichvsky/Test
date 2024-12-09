import random


class ua_lang:
    themes = ["theme1","theme2",
              "theme3","theme4",
              "theme5"]
class algebra:
    themes = ["theme1","theme2",
              "theme3","theme4",
              "theme5"]

class Student(ua_lang,algebra):
    def __init__(self,name:str,form:int):
        self.name = name
        self.form = form
        self.marks = {}

    def set_marks(self):
        #subject = str(input("Оберіть предмет: "))
        subject = "укр мова"
        if subject == "укр мова":
            marks = [random.randint(1,5) for _ in range(5)]

            self.marks["Subject ua_lang"] = dict(zip(ua_lang.themes,marks))
            print(self.marks)
d = Student("danya",5)
d.set_marks()
