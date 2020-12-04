input_list = []
number = input()
while not number == "STOP":
    input_list.append(int(number))
    number = input()

for i in input_list:
    for j in input_list:
        k = 2020 - i - j
        if k in input_list:
            print(i, j , k, i*j*k)
