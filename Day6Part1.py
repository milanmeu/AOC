file = open("input6")

yes = 0

line = file.readline()

while line:
    yes_questions = set()
    while line and line != "\n":
        for letter in line:
            if letter != "\n":
                yes_questions.add(letter)
        line = file.readline()
    yes += len(yes_questions)
    yes_questions = set()
    line = file.readline()
print(yes)
file.close()
