file = open("input4.txt")
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
total_valid = 0

line = file.readline()

while line:
    document = ""
    while line and line != "\n":
        document = document + line
        line = file.readline()
    if all(x in document for x in keys):
        valid = True
        for field in document.split():
            key_value = field.split(":")
            key = key_value[0]
            value = key_value[1]
            if not (\
                    (key == "byr" and 1920 <= int(value) <= 2002) \
                            or (key == "iyr" and 2010 <= int(value) <= 2020) \
                            or (key == "eyr" and 2020 <= int(value) <= 2030) \
                            or (key == "hgt" and \
                                ((("cm" in value) and (150 <= int(value[:-2]) <= 193))
                                 or (("in" in value) and (59 <= int(value[:-2]) <= 76)))) \
                            or (key == "hcl" and value[:1] == "#" and len(value) == 7) \
                            or (key == "ecl" and value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")) \
                            or (key == "pid" and len(value) == 9 and value.isnumeric()) \
                            or (key == "cid")):
                valid = False
        if valid:
            total_valid += 1
    line = file.readline()
print(total_valid)
file.close()
