name = input("Enter your name: ")
surname = input("enter your surname: ")

print(name, surname)

# ამოცანა 1: შეიყვანეთ ორი რიცხვი და გამოიტანოს მათი ჯამი. რადგან სტრინგებს ვერ შეკრებს, დავამატეთ int ელემენტი
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

print (num1 + num2)

# ამოცანა 2: იუზერს შემოაქ 3 ცვლადი
# აage, name, surname 
#format-ით უნდა დაიწეროს: Hello, "name", your surname is "sruname, and your age is "age"

age = input("enter your age: ")
name = input("enter your name: ")
surname = input("enter your surname: ")
my_text = "Hello, {}, your surname is {} and your age is {}"

print (my_text.format(name, surname, age))
