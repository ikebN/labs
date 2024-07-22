def balance(expression):
    scobki = []
    dic_scob = {')': '(', ']': '[', '}': '{', '>': '<'}

    for char in expression:
        if char in '([{<':
            scobki.append(char)
        elif char in ')]}>':
            if not scobki or scobki.pop() != dic_scob[char]: return False
    return not scobki


try:
    with open("input.txt", 'r') as file:
        expressions = file.readlines()
except FileNotFoundError:
    print(f"File 'input.txt' not found")



results = []

for expression in expressions:
    results.append(balance(expression.strip()))

try:
    with open('output.txt', 'w') as file:
        for result in results:
            file.write(f"{result}\n")
    print(f"The results have been successfully written to 'output.txt'")
except IOError as e:
    print(f"File write error: {e}")