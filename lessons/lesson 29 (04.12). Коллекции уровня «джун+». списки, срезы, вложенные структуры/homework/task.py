#Работа со списками
main_dishes = ["стейк", "паста", "салат"]
desserts = ["чизкейк", "мороженое", "тирамису"]

main_dishes.insert(3, desserts[0])
main_dishes.insert(4, desserts[1])
main_dishes.insert(5, desserts[2])

print(f'Общее количество блюд: {len(main_dishes)}')
print(f'Первое блюдо: {main_dishes[0]}')
print(f'Последнее блюдо: {main_dishes[-1]}')

for i in range(len(main_dishes)):
    print(f'{i+1}. {main_dishes[i]}')

#Срезы
orders = [101, 102, 103, 104, 105, 106, 107, 108, 109]
print(f'\nПервые четыре заказа: {orders[:4]}')
print(f'Последние три заказа: {orders[-3:]}')
print(f'Каждый второй заказ, начиная с первого: {orders[::2]}')
print(f'Cписок без первого и последнего заказа: {orders[1:-1]}')

#Мутация списков
ingredients = ["лук", "морковь", "картофель", "томаты"]

ingredients.extend(["соль", "перец"])
ingredients.insert(2, 'чеснок')

if "лук" in ingredients:
    ingredients.remove("лук")

last_ingredient = ingredients.pop()
ingredients.insert(0, last_ingredient)
print(f'\n{ingredients}\n')

#Вложенные структуры
menu = [
    {"название": "стейк", "тип": "основное", "цена": 800},
    {"название": "паста", "тип": "основное", "цена": 450},
    {"название": "чизкейк", "тип": "десерт", "цена": 300},
    {"название": "тирамису", "тип": "десерт", "цена": 350}
]

for dish in menu:
    print(f"{dish['название']}: {dish['тип']} ({dish['цена']} руб)")

expensive_dishes = []
for dish in menu:
    if dish['цена'] > 500:
        print(f"\nБлюда дороже 500 рублей: {dish['название']}\n")

desserts = []
print('Десерты:')
for dish in menu:
    if dish['тип'] == 'десерт':
        print(f"{dish['название']}: {dish['тип']} ({dish['цена']} руб)")

total_price = 0
for dish in menu:
    total_price += dish["цена"]
average_price = total_price / len(menu)
print(f"\nСредняя цена блюда: {average_price:.2f} руб")



