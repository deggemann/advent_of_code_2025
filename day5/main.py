from functools import reduce
import operator

def load_data(path):
    lines = []
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    
    numbers = lines[:-1]
    operations = lines[-1]

    operations = operations.replace(" ", "")
    lines = [line.split(" ") for line in lines[:-1]]

    cleaned_lines = []
    for line in lines:
        cleaned_lines.append([number for number in line if number != ""])

    return cleaned_lines, list(operations)

def load_data_second_star(path):
    lines = []
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    
    numbers = lines[:-1]
    operations = lines[-1]

    operations = operations.replace(" ", "")

    cleaned_lines = []
    tmp_numbers = []
    for column in range(len(numbers[0])-1, 0, -1):
        if numbers[0][column] == " ":
            cleaned_lines.append(tmp_numbers)
            tmp_numbers = []
            continue
        tmp_number = []
        for row in range(4):
            if numbers[row][column] != " ":
                tmp_number.append(numbers[row][column])
        tmp_numbers.append(int("".join(tmp_number)))
        

    return cleaned_lines, list(operations)
    

if __name__ == "__main__":
    PATH = "day5/input.txt"
    numbers, operations = load_data(PATH)

    print(f"Operations: {operations[:20]}")
    print(f"Numebrs: {numbers[0][:20]}")

    for i, line in enumerate(numbers):
        print(f"Length of number {i} is {len(line)}")

    print(f"Length of operations: {len(operations)}")

    total = 0
    while operations:
        if operations.pop() == "*":
            total += int(numbers[0].pop()) * int(numbers[1].pop()) * int(numbers[2].pop()) * int(numbers[3].pop())
        else:
            total += int(numbers[0].pop()) + int(numbers[1].pop()) + int(numbers[2].pop()) + int(numbers[3].pop())

    print(f"Total is: {total}")

    # -------------------- second start -----------------------------

    # note: sometimes numbers start from top sometimes the top is " " but below
    # there are numbers, this is not taken into consideration when reading the numebrs

    numbers, operations = load_data_second_star(PATH)
    operations = list(reversed(operations))
    total = 0
    for i, nbr_list in enumerate(numbers):
        if operations[i] == "+":
            total += sum(nbr_list)
        elif operations[i] == "*":
            total += reduce(operator.mul, nbr_list)
        else:
            raise ValueError(f"Recieved operation {operations[i]}")

    print(f"Total of all calculations: {total}")
    