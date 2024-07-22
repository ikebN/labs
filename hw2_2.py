try:
    with open('input2.txt', 'r') as file:
        lines = file.readlines()

    symb = input("Enter the symbols: ")

    backwards_lines = []
    for line in lines:
        line = line.rstrip()

        while line and line[-1] in symb:
            line = line[:-1]
        line = line + ';'
        backwards_lines.append(line[::-1])

    with open('output2.txt', 'w') as file:
        for line in backwards_lines:
            file.write(line + '\n')

except FileNotFoundError:
    print("File 'input2.txt' not found")