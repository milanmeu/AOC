file = open("input6")

yes = 0

line = file.readline()

while line:
    yes_group = set()
    for letter in line:
        if letter != "\n":
            yes_group.add(letter)
    line = file.readline()
    while line and line != "\n":
        yes_person = set()
        for letter in line:
            if letter != "\n":
                yes_person.add(letter)
        yes_group.intersection_update(yes_person)
        line = file.readline()
    yes += len(yes_group)
    line = file.readline()
print(yes)
file.close()
