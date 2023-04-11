num = int(input('Введите необходимое количество билетов: '))
ages = []

for i in range(0, num):
    a = int(input("Введите возраст участников: "))
    ages.append(a)
def prise(a):
    if a < 18:
        return 0
    elif 18 <= a < 25:
        return 990
    else:
        return 1390
pr = sum(map(prise, ages))
dpr = int(pr*0.9)
if num > 3:
    print("Стоимость всех билетов со скидкой: ", dpr, "руб.")
else:
    print("Стоимость всех билетов: ", pr, "руб.")
