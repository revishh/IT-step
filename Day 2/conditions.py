#ამოცანა : ჩაწეროს იუსერმა რიცხვები და მნიშვნელობების მიხედვით ამოაგდოს შედეგები

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

if num1>num2:
    print("num1 is greater")
elif num2>num1:
    print("num2 is greater")
else:
    print("num1 and num2 are equal")
    
#შემოვა რიცხვი, თუ ეს რიცხვი იქნება ლუწი, დაიპრინტოს "ლუწია", თუ კენტი, დაიპრინტოს "კენტია"

number = int(input("Enter your number: "))

if number%2==0:
    print("ლუწია")
else:
    print("კენტია")
    
    
#ამოცანა 2: თუ რიცხვი არის ლუწი და 10-სა და 30-ს შორის, მას ქვია ჯიგარი
number = int(input("Enter your number: "))

if number<=30 and number>=10 and number%2==0:
    print("ჯიგარია")
else:
    print("ჩათლახია")
    
    
    #შეიძლება ასეც
number = int(input("Enter your number: "))
    
if number%2==0 and number>10 and number<30:
    print("ჯიგარია")
else:
    print("ჩათლახია")   

 
# nested conditional
number = int(input("Enter your number: "))

if number>10 and number<30:
    if number%2==0:
        print("ჯიგარია")
else:
    print("არაა ჯიგარი")
        
        
            