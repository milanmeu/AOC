file = open("input4.txt")
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0

line = file.readline()

while line:
    document = ""
    while line and line != "\n":
        document = document + line
        line = file.readline()
    if all(x in document for x in keys):
        valid += 1
    line = file.readline()
print(valid)
file.close()
