def add_task(task_list, description, tags = None):
    if tags is None:
        tags = []
    new_task = {"description": description, "tags": tags}
    task_list.append(new_task)


def create_report(task_list = False, sort_by_desc = False, header="Отчет по задачам"):
    work_list = list(task_list)
    if sort_by_desc:
        work_list.sort(key=lambda task: task["description"])
    report_text = f'{header}\n'
    for task in work_list:
        for i in range(work_list.index(task), len(work_list)):
            report_text += f" {i+1}. {task['description']} {task['tags']}\n"
            break
    return report_text


my_tasks = []

# Вызов 1: Добавление задачи с тегами
add_task(my_tasks, "Купить молоко", ["дом", "срочно"])
print(my_tasks)

# Вызов 2: Добавление задачи без тегов (используется значение по умолчанию)
add_task(my_tasks, "Позвонить маме")
print(my_tasks)

# Вызов 3: Еще один вызов без тегов. Убедимся, что списки тегов разных задач независимы.
add_task(my_tasks, "Прочитать книгу")
my_tasks[1]["tags"].append("семья")  # Добавим тег только ко второй задаче
print(my_tasks)


test_list = [
        {'description': 'Закончить проект', 'tags': ['работа']},
        {'description': 'Записаться к врачу', 'tags': ['здоровье']},
        {'description': 'Апгрейд ПК', 'tags': ['хобби', 'дорого']}
    ]

#Вызов 1: Все аргументы по порядку (позиционно)
print(create_report(test_list, True, "Важные дела"))

#Вызов 2: Позиционный `task_list` и именованные аргументы в разном порядке
print(create_report(test_list, header="Мой план", sort_by_desc=True))

#Вызов 3: Только обязательный аргумент, остальные — по умолчанию
print(create_report(test_list))
