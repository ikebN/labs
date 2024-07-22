input_1 = 'input1.txt'
input_2 = 'input2.txt'
output_file = 'output.txt'

with open('output.txt', 'w') as dest:
    pass


def copy(input_file, output_file):
    try:
        with open(input_file, 'r') as input:
            with open(output_file, 'a') as output:
                for line in input:
                    output.write(line.strip() + '\n')

    except FileNotFoundError:
        print(f"File {input_file} not found")

copy(input_1, output_file)
copy(input_2, output_file)

with open(output_file, 'r') as file:
    lines = file.readlines()
lines.sort()

with open(output_file, 'w') as file:
    for line in lines:
        file.write(line)