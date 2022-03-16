#user-ს ვეკითხებით: name , surname , grade -ს
#თუ სახელში ორზე მეტჯერ აქვს "i" 
#და გვარი მთავრდება "shvili"-ზე 
#და ქულა მეტია 50-ზე დაპრინტოს დაფორმატებული ტქსტით "You win name, surname"
#else : "you lose name, surname"

name = input("Enter your name: ")
surname = input("Enter your surname: ")
grade = int(input("Enter your grade: "))
my_text = "{} {}, you win, yout grade is {}"
my_text2 = "{} {}, you lose, yout grade is {}"
if (name.count("i"))>=2 and surname[-6:]=="shvili" and grade>50:
    print(my_text.format(name, surname, grade))
else:
    print(my_text2.format(name, surname, grade))
    
    
    


