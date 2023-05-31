tickets = 1
q = (int(input("Введите количество билетов:")))
for age in range(q):
    age = (int(input("Введите возраст посетителя:")))
    if age < 18:
        tickets = q * 0
    elif age >= 18 and age < 25:
        tickets = q * 990
    elif age >= 25:
        tickets = q * 1390
print("Стоимость Ваших билетов", tickets)
if q > 3:
    tickets = tickets - tickets / 100 * 10
    print("Стоимость Ваших билетов", tickets)




