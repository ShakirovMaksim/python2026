shifts = [('team-A', 40), ('team-B', 32), ('team-A', 15), ('team-C', 20)]
finished = ['team-B']

boxes = {}

for team, count in shifts:
    boxes[team] = boxes.get(team, 0) + count

for team in finished:
        boxes.pop(team, 0)
        print(f'Закончила раньше всех бригада: {team}')
print(boxes)
