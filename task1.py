string = input("Введите текст: ")
 
dlina = len(string)
 
lower = upper = 0
 

for i in string:
    if i.islower():
        lower += 1
        print(lower)
    elif i.isupper():
        upper += 1
        print(upper)
 
per_lower = lower / dlina * 100
per_upper = upper / dlina * 100
print("Lower: %.2f%%" % per_lower)
print("Upper: %.2f%%" % per_upper)

