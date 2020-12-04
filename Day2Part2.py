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
    fl = password[low-1:low]
    sl = password[high-1:high]
    print(fl, sl, letter)
    if (fl == letter) ^ (sl == letter):
        valid += 1
    print(valid)
    line = input()
