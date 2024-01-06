input = open("01/input.txt", "r")

array = []

values = []

result = 0

for line in input:

    line = line.strip("\n")

    line = line.replace("oneight", "oneeight")
    line = line.replace("twone", "twoone")
    line = line.replace("threeight", "threeeight")
    line = line.replace("fiveight", "fiveeight")
    line = line.replace("sevenine", "sevennine")
    line = line.replace("nineight", "nineeight")
    line = line.replace("eightwo", "eighttwo")

    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")

    array.append(line)

for item in array:

    single_value = ""

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
