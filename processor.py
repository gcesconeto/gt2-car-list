import sys
import os.path

car_separator = "="
car_separator = car_separator.rjust(77, '=')


def txt_importer(path_file):
    if path_file[-3:] != "txt":
        return print("invalid format", file=sys.stderr)
    if not os.path.isfile(path_file):
        return print(f"{path_file} not found", file=sys.stderr)
    with open(path_file, 'r') as file:
        line_list = file.read()
        return line_list.split('\n')


def processor(lines):
    output = []
    are_cars = False
    brand = ""
    for index in range(len(lines)):
        if lines[index] == car_separator:
            are_cars = True
            brand = lines[index - 4]
        if lines[index] == "" and lines[index - 1] == "":
            are_cars = False
        if are_cars and len(lines[index]) == 75:
            new_line = brand + ","
            new_line += (lines[index][0:37].strip() + ",")
            new_line += (lines[index][38:40].strip() + ",")
            new_line += (lines[index][41:44].strip() + ",")
            new_line += (lines[index][45] + ",")
            new_line += (lines[index][47:51].strip() + ",")
            new_line += (lines[index][53:57].strip() + ",")
            new_line += (lines[index][59:63].strip() + ",")
            new_line += (lines[index][65:69].strip() + ",")
            new_line += (lines[index][71:75].strip() + "\n")
            output.append(new_line)
    return output


input_lines = txt_importer("data.txt")

output_lines = processor(input_lines)

with open("output.csv", "w") as file:
    file.writelines(output_lines)
