base_workout = ["кардио", "пресс", "растяжка"]
coach = ["планка", "йога"]

base_workout.insert(3, coach[0])
base_workout.insert(4, coach[1])

total_exercises = len(base_workout)  #Всего упражнений
third = base_workout[2]  #Третье упражнение
penultimate = base_workout[-2]  #Предпоследнее упражнение

print(f"""
Всего упражнений: {total_exercises}
Третье: {third}
Предпоследнее: {penultimate}""")

for i in range(len(base_workout)):
    print(f"{i+1}. {base_workout[i]}")
