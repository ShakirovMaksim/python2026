# Уровень 1. Базовый

## Задача

Прочитать CSV-файл с данными о студентах и вывести средний балл по каждому предмету.

### Пример данных (`students.csv`)

```csv
Name,Math,Physics,Chemistry
Alice,85,90,78
Bob,75,80,85
Charlie,95,88,92
```

### Результат

```
Math: 85.0
Physics: 86.0
Chemistry: 85.0
```

---

# Уровень 2. Средний

## Задача

Есть JSON-файл с данными о сотрудниках компании (имя, отдел, зарплата). Нужно написать программу, которая:
- выводит общую сумму зарплат для каждого отдела;
- сохраняет результаты в новый JSON-файл.

### Пример данных (`employees.json`)

```json
[
    {"name": "Alice", "department": "IT", "salary": 5000},
    {"name": "Bob", "department": "IT", "salary": 4500},
    {"name": "Charlie", "department": "HR", "salary": 4000},
    {"name": "Diana", "department": "HR", "salary": 4200},
    {"name": "Eve", "department": "Finance", "salary": 5200}
]
```

### Результат

```
IT: 9500
HR: 8200
Finance: 5200
```

### Новый файл (`department_salaries.json`)

```json
{
    "IT": 9500,
    "HR": 8200,
    "Finance": 5200
}
```

---

# Уровень 3. Продвинутый

## Задача

Дано два файла:
- в `products.csv` содержатся данные о количестве продуктов;
- в `prices.json` указаны цены этих продуктов.

Нужно создать новый JSON-файл, в котором будут указаны продукты, их количество и общая стоимость.

### Пример данных (`products.csv`)

```csv
Product,Quantity
Apples,10
Oranges,5
Bananas,7
```

### Пример данных (`prices.json`)

```json
{
    "Apples": 2.5,
    "Oranges": 3.0,
    "Bananas": 1.5
}
```

### Результат (`products_total.json`)

```json
{
    "Apples": {
        "quantity": 10,
        "total_price": 25.0
    },
    "Oranges": {
        "quantity": 5,
        "total_price": 15.0
    },
    "Bananas": {
        "quantity": 7,
        "total_price": 10.5
    }
}
```
