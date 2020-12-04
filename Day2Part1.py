input_list = []
line = input()
valid = 0
while True:
    low = int(line[:line.index("-")])
    high = int(line[line.index("-")+1:line.index(" ")])
    dubbelpunt = line.index(":")
    letter = line[line.index(" ")+1:dubbelpunt]
    password = line[line.index(" ",dubbelpunt)+1:]
    teller = 0
    for i in password:
        if i == letter:
            teller += 1
    if low <= teller <= high:
        valid += 1
    print(valid)
    line = input()
