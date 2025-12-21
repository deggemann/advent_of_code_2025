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

if __name__ == "__main__":
    PATH = "day5/input.txt"
    numbers, operations = load_data(PATH)

    print(f"Operations: {operations[:20]}")
    print(f"Numebrs: {numbers[0][:20]}")

    for i, line in enumerate(numbers):
        print(f"Length of number {1} is {len(line)}")

    print(f"Length of operations: {len(operations)}")

    total = 0
    while operations:
        if operations.pop() == "*":
            total += int(numbers[0].pop()) * int(numbers[1].pop()) * int(numbers[2].pop()) * int(numbers[3].pop())
        else:
            total += int(numbers[0].pop()) + int(numbers[1].pop()) + int(numbers[2].pop()) + int(numbers[3].pop())

    print(f"Total is: {total}")

    