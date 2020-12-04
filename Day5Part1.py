import math

boarding_passes = []
text = input()
highest_seat_id = 0
seat_ids = []

while text != "END":
    boarding_passes.append(text)
    text = input()

for boarding_pass in boarding_passes:
    row = (0, 127)
    column = (0, 7)
    for character in boarding_pass[:7]:
        middle = (row[0] + row[1]) / 2
        if character == "F":
            row = (row[0], math.floor(middle))
        elif character == "B":
            row = (math.ceil(middle), row[1])

    for character in boarding_pass[7:]:
        middle = (column[0] + column[1]) / 2
        if character == "L":
            column = (column[0], math.floor(middle))
        elif character == "R":
            column = (math.ceil(middle), column[1])
    seat_id = int(row[0] * 8 + column[0])
    seat_ids.append(seat_id)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

for seat_id in range(0, highest_seat_id):
    if (seat_id not in seat_ids) and (seat_id + 1 in seat_ids) and (seat_id - 1 in seat_ids):
        print("Missing seat ID", seat_id)
print("Highest seat ID: ", highest_seat_id)
