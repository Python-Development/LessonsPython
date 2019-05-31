# Програма вітання

age = 0
# перевіряю щоб вводили тільки цифри (щоб трохи ускладнити)
while True:
    getAge = input("Скільки вам років? ")
    if getAge.isdigit():
        age = int(getAge)
        break
    else:
        print("Недопустимі символи!!!")
        print("Спробуйте ще раз:")

if age < 16:
    print("Привіт!")
elif (age >= 16) and (age <= 30):
    print("Вітання!")
else:
    print("Добрий день.")
