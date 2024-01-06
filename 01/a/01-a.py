input = open("01/input.txt", "r")

array = []

values = []

result = 0

for line in input:
    array.append(line.strip('\n'))

for item in array:

    single_value = ''

    for character in item:
        if character.isdigit():
            single_value += character
            break

    for character in item[::-1]:
        if character.isdigit():
            single_value += character
            break

    values.append(int(single_value))

for value in values:
    result += value

print(result)
