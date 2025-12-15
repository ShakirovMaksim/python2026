def calculate_average(evaluations):
    return sum(evaluations) / len(evaluations)

def check_excellent(calculated_average):
    if calculated_average > 4.5:
        return 'Отличник'
    else:
        return 'Не отличник'

total = calculate_average(evaluations=[5,4,5,5,5])
print(f'Средний балл: {total}')
print(f"Статус: {check_excellent(total)}")
