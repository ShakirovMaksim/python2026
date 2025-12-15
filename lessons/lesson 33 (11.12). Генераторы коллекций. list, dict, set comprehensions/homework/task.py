#Задача №1
orders = [("Степан", 72000, "Самара"), ("Кира", 18000, "Казань"), ("Яна", 95000, "Сочи")]
result = [
    f"{name} {'купила' if name[-1] in 'ая' else 'купил'} на {amount // 1000}d{'K' if amount >= 70_000 else '₽'}"
    for name, amount, city in orders
    if city.lower().startswith(('c', 'k'))
]
print(result)

#Задача №2
returns = [
    {"id": 101, "status": "pending", "items": 3, "reason": "size"},
    {"id": 102, "status": "processing", "items": 2, "reason": ""},
    {"id": 103, "status": "pending", "items": 1, "reason": "color"}
]
positions_map = {1: "позицию", 2: "позиции", 3: "позиции", 4: "позиции"}
result = [
    f"Возврат #{item['id']}: {positions_map.get(item['items'], '')} ({item['reason']})"
    for item in returns
    if item["status"] == "pending" and 1 <= item["items"] <= 4 and item["reason"]
]
print(result)

#Задача №3
import math

departments = [
    {
        "name": "Support",
        "budget": 300000,
        "employees": [
            {"name": "John", "salary": 60000, "remote": True},
            {"name": "Jane", "salary": 70000, "remote": False},
            {"name": "Alice", "salary": 80000, "remote": True}
        ]
    },
    {
        "name": "Sales",
        "budget": 200000,
        "employees": []
    }
]
dept_summary = {
    d["name"]: (
        math.ceil(sum(e["salary"] for e in d["employees"]) / len(d["employees"])),
        round(len([e for e in d["employees"] if e["remote"]]) / len(d["employees"]), 2),
    )
    for d in departments
    if len(d["employees"]) >= 3 and sum(e["salary"] for e in d["employees"]) <= d["budget"]
}

print(dept_summary)

#Задача №4
logs = ["alex:upload:180", "ben:sync:75", "lana:sync:135", "max:update:300"]
filtered_users = {
    parts[0]
    for log in logs
    if (parts := log.split(':')) and len(parts) == 3 and parts[1] in ('upload', 'sync') and int(parts[2]) > 120
}
print(filtered_users)
