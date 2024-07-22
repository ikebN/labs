while True:
    try:
        mil_pops = int(input("Enter the number of minimal population: "))
        break
        cities1 = []

        with open('cities.txt', 'r') as file:
            for line in file:
                city, population = line.strip().split(':')
                if int(population) > mil_pops:
                    cities1.append((city, int(population)))
        cities1.sort(key=lambda x: x[0])

        with open('filtered_cities.txt', 'w') as file:
            for city, population in cities1:
                file.write(f"{city}:{population}\n")
    except ValueError:
        print("Incorrect input. Please enter a number")


