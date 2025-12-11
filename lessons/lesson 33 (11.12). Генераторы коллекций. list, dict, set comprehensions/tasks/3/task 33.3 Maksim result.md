result: 40/100

### 1. Формулировка задания
Требуется создать словарь `dept_summary` с помощью dict comprehension, где для каждого отдела из списка `departments` сохраняется кортеж `(средняя_зарплата, доля_удалённых)`.  
**Условия**:  
- Средняя зарплата округляется вверх до целого (`math.ceil`).  
- Доля удалённых сотрудников округляется до двух знаков (`round(value, 2)`).  
- Включать только отделы с ≥3 сотрудниками и бюджетом ≥ суммарной зарплаты.  
- Решение должно быть реализовано одним dict comprehension.  

---

### 2. Результаты проверки
**Файл**: `task.py` (строки 25-30)  
**Код студента**:
```python
dept_summary = {
    name: (avg_salary(employees), remote_percentage(employees))
    for name, budget, employees in departments
    if len(employees) >= 3 and budget > total_salary(employees)}
```

**Ошибки**:  
1. **Блокирующая ошибка**: Неправильное извлечение данных из словаря `departments`.  
   - Строка `for name, budget, employees in departments` пытается распаковать словарь как кортеж, что вызовет `ValueError`.  
   - **Как воспроизвести**: Запуск кода приведёт к ошибке:  
     ```python
     ValueError: too many values to unpack (expected 3)
     ```  

2. **Значимая ошибка**: Неверное условие для проверки бюджета.  
   - Используется `budget > total_salary(employees)`, тогда как по условию нужно `budget >= total_salary`.  
   - **Пример**: Если бюджет равен суммарной зарплате, отдел не попадёт в результат, хотя должен.  

---

### 3. Сильные стороны работы
- **Читаемость**: Код разделён на вспомогательные функции (`total_salary`, `avg_salary`, `remote_percentage`), что улучшает понимание логики.  
- **Корректность округлений**:  
  - Средняя зарплата округляется вверх с помощью `math.ceil`.  
  - Доля удалённых сотрудников округляется до двух знаков через `round`.  
- **Проверка условий**: Правильно проверяется количество сотрудников (`len(employees) >= 3`).  

---

### 4. Ошибки и способы исправления
**Блокирующие ошибки** (критичные, код не работает):  
1. **Неправильная распаковка данных из `departments`**:  
   - **Исправление**: Заменить распаковку на обращение по ключам словаря.  
   ```python
   dept_summary = {
       dept["name"]: (avg_salary(dept["employees"]), remote_percentage(dept["employees"]))
       for dept in departments
       if len(dept["employees"]) >= 3 and dept["budget"] >= total_salary(dept["employees"])
   }
   ```

**Значимые ошибки** (нарушение логики условия):  
2. **Неверное условие для бюджета**:  
   - **Исправление**: Заменить `>` на `>=`.  
   ```python
   if len(dept["employees"]) >= 3 and dept["budget"] >= total_salary(dept["employees"])
   ```

---

### 5. Оценка
**Функциональность (50%)**: 0/50  
- Код не работает из-за блокирующей ошибки (неверная распаковка данных).  
- Условие по бюджету реализовано неверно.  

**Качество кода (30%)**: 15/30  
- Логика вспомогательных функций корректна, но основная часть (comprehension) содержит ошибки.  

**Стиль и тесты (20%)**: 18/20  
- Код читаем, но отсутствуют комментарии и тесты (хотя это не требовалось).  

**Итог**: 40/100  
- Снято 60%: 50% за неработающую функциональность, 10% за логические ошибки.  

---

### 6. Полное решение
```python
import math

def total_salary(employees):
    return sum(emp["salary"] for emp in employees)

def avg_salary(employees):
    avg = total_salary(employees) / len(employees)
    return math.ceil(avg)

def remote_percentage(employees):
    remote_count = sum(emp["is_remote"] for emp in employees)
    return round(remote_count / len(employees), 2)

dept_summary = {
    dept["name"]: (avg_salary(dept["employees"]), remote_percentage(dept["employees"]))
    for dept in departments
    if len(dept["employees"]) >= 3 and dept["budget"] >= total_salary(dept["employees"])
}
```

---

Анализ выполнен моделью: GPT-4o.
