rooms = [
    ('Omega', '2025-12-05 14:00'),
    ('Delta', '2025-12-05 16:30'),
    ('Atlas', '2025-12-04 11:15'),
]
room_to_check = 'Delta'
new_room = 'Nova'

last_booking = {}
for name, time in rooms:
    last_booking[name] = time

delta = last_booking.get(room_to_check)
nova = last_booking.get(new_room, 'еще свободна')

print(f"{room_to_check} -> {delta}")
print(f"{new_room} -> {nova}")
