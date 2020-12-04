input_list = []
text_input = input()
while text_input != "STOP":
    input_list.append(list(text_input))
    text_input = input()

totaal_bomen = 1

right = input()
while right != "STOP":
    right = int(right)
    down = int(input())
    table = list(input_list)

    while len(table[0]) * down < len(input_list) * right:
        for i in range(len(input_list)):
            table[i] = table[i] + input_list[i]

    x = right
    y = down
    bomen = 0

    while len(table) > y:
        if table[y][x] == "#":
            bomen += 1
        x += right
        y += down
    print(bomen)
    totaal_bomen *= bomen
    right = input()

print(totaal_bomen)
