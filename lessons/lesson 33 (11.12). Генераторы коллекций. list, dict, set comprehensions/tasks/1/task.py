orders = [
    ("Николай", 32000, "Казань"),
    ("Анна", 52000, "Самара"),
    ("Ирина", 61000, "Калуга"),
    ("Марк", 15000, "Кемерово")
]
result = [
    f"{name} {'купила' if name[-1] in ('а', 'я') else 'купил'} на {amount} руб."
    for name, amount, city in orders
    if city.lower().startswith("к")

]
print(result)
