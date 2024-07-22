try:
    summ = 0
    lines = 0
    with open('input1.txt', 'r') as file:
        for line in file:
            lines += 1
            summ += int(line.split(',')[1])
    average = summ / lines
    with open('input1.txt', 'r') as file:
        with open('output1.txt', 'w') as file2:
            for line in file:
                if int(line.split(',')[1]) >= average:
                    file2.write(line)
except FileNotFoundError:
    print("File 'input.txt' not found")