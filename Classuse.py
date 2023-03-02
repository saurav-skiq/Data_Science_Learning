class Human:
    def __init__(self, name, occupation) -> None:
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name," Plays tennis")

        if self.occupation == "Actor":
            print(self.name," Plays Acts")

tom= Human('Tom Cruise','Actor')

tom.do_work()
#Excercise

class Employee:
    def __init__(self,id, name) -> None:
        self.id= id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")

emp= Employee(1, 'Coder')
emp.display()
print("------------------------")
del emp.id
print('-------------------------')
try:
    emp.display()
except AttributeError:
    print("Emp is not defined")