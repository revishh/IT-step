#დაბერება ათი წლით
#დაამატეთ ახალი წყვილი: had_gf = true
#ამოაგდეთ ლოკაცია
#გაასუფთავეთ

my_dict = {
    "name":"mari",
    "surname":"Revishvili",
    "age":int("24"),
    "location":"Tbilisi",
    "children":["gio","mari"]
}

my_dict["age"]="34"

my_dict.pop("location")
my_dict["has_gf"]="true"
my_dict.clear()
print(my_dict)
