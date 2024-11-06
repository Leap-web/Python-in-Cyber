print("Thay_Bunleap_G2_W05")
print("Exercise 1")
class Car:

    # Attribute
    make = "Toyota"
    model = "Corolla"
    year = 2024
    
    def display_info(self):
        print("Car details")
        print("Make: {}".format(self.make))
        print("Model: {}".format(self.model))
        print("Year: {}".format(self.year))

Car_details = Car()
Car_details.display_info()

print("\nExercise 2")
class Cars:
    
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
    
    def is_vintage(self, object_name):
        if ((2024 - self.year) <= 25):
            print(f"{object_name} is vintage: False")
        else:
           print(f"{object_name} is vintage: True")

Car_1 = Cars("Toyota", "Corolla", 1999)
Car_2 = Cars("BMW", "i8", 1997)

Car_1.is_vintage("Car_1")
Car_2.is_vintage("Car_2")


print("\nExercise 3")
class Student:
    name = "John"
    age = 20
    old_grade = "B"

    def update_grade(self, new_grade):
        self.grade = new_grade
        print("Before grade update: ")
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Grade: {}".format(self.old_grade))
        print("After grade updated: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {new_grade}")
        
student = Student()
new_grade = ("A")
student.update_grade(new_grade)

print("\nExercise 4")
class BankAccount:
    owner = "John"
    old_amount = 1000

    def deposit(self, deposit):
        self.deposit_amount = deposit
        self.new_amount = self.deposit_amount + self.old_amount
        print("Initial balance for John: ${}".format(self.old_amount))
        print("\nDepositing: ${}".format(deposits))
        print("New balance: ${}".format(self.new_amount))
        
    def withdraw(self, withdraw, deposit):
        self.with_amount = withdraw
        self.deposit_amount =  deposit
        self.new_amount = self.deposit_amount + self.old_amount
        self.final_amount = self.new_amount -  self.with_amount

        if with_draw > self.new_amount:
            print("\nAttempting to withdraw : ${}".format(with_draw))
            print("Insufficient funds. Withdrawal failed.")
            print("\nFinal balance: ${}".format(self.new_amount))
        else:
            print("\nWithdrawing: ${}".format(with_draw))
            print("New balance: ${}".format((self.new_amount - self.with_amount)))
            print("\nFinal balance: ${}".format(self.final_amount))
        
Depositing = BankAccount()
deposits = (500)
Depositing.deposit(deposits)

Withdraw = BankAccount()
with_draw = (300)
Withdraw.withdraw(with_draw, deposits)

print("\nExercise 5")
class Book:
    def __init__ (self, title, author, price):
        self.title = title 
        self.author = author 
        self.price = price

class Library(Book):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print("Title: {}, Author: {}, Price: ${}".format(book.title, book.author, book.price))

library = Library()

book1 = Book("The Great Man", "F. Ane Fit", 10.99)
book2 = Book("The story about APT", "Fake Man", 12.50)
book3 = Book("1984", "George Orwell", 9.75)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

print("\nExercise 6")
class Classroom:
    def __init__ (self, class_name, students=None):
        self.class_name = class_name
        self.students = students if students is not None else []

    def add_student(self, students):
        self.students.append(students)

    def list_students(self):
        for student in self.students:
            print("Added student: {}".format(student))
        print("Students in {}:".format(self.class_name))
        for student in self.students:
            print("- {}".format(student))

math = Classroom("Math 101")

math.add_student("Alice")
math.add_student("Bob")
math.add_student("Charlie")

math.list_students()

print("\nExercise 7")
class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def display_contact(self):
        for name,  number in self.contacts.items():
            print("Add contact: {} -> {}".format(name, number))

    def find_contact(self, name):
        if name in self.contacts:
            return "{}'s number: {}".format(name, self.contacts[name])
        else:
            return "{} not found in phone book.".format(name)
    
contact = PhoneBook()

contact.add_contact("John", "123-456-7890")
contact.add_contact("Jane", "987-654-3210")

contact.display_contact()

print(contact.find_contact("John"))
print(contact.find_contact("Alice"))