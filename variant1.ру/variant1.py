

boarding = int(input("посадка")










text = input("Число: ")
number = int(text)
print(type(text))
print(type(number))
print("цифр", len(text))
print("Число x 2", text * 2)
print("строка x 2", text * 2)



domain = input("Домен: ")
section = input("Раздел: ")
page = input("страница: ")

print("https:/", domain, section, page, sep="/")
print("Вы здесь:", end=" ")
print(section, page, sep=" > ")



distance = int(input("Расстояние, км: "))
per_100 = int(input("Расход на 100 км, л: "))
price = int(input("Цена литра, руб.: "))

liters = (distance * per_100) / 100

cost = liters * price

print("Понадобится литров: ", liters)
print("Стоимость бензина:", cost, "руб.")


#6

before = int(input("Позавчера:"))
yesterday = int(input("Вчера"))
today = int(input("Сегодня: "))

print("Прирост вчера: ", yesterday - before)

before, yesterday = yesterday, today 

print("Прирост сегодня: ", yesterday - before)

#7

balance = int(input("Баланс, руб.: "))