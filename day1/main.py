
def load_data(path):
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    return lines

def dial_step(dial_value: int, direction: int):
    dial_value = dial_value + 1 * direction
    at_zero = False
    if dial_value == -1:
        dial_value = 99
    if dial_value == 100:
        dial_value = 0
    if dial_value == 0:
        at_zero = True
    return dial_value, at_zero

def move_dial(dial_value: int, move: str):
    direction = 1 if move[0] == "R" else -1
    steps = int(move[1:])
    n_passed_zero = 0
    for step in range(int(steps)):
        dial_value, at_zero = dial_step(dial_value, direction)
        n_passed_zero += at_zero
    return dial_value, n_passed_zero

if __name__ == "__main__":
    PATH = "input.txt"
    lines = load_data(PATH)

    dial_value = 50
    password_count = 0
    n_passed_zero = 0 
    for move in lines:
        dial_value, new_passed_zero = move_dial(dial_value, move)
        n_passed_zero += new_passed_zero

        if dial_value == 0:
            password_count += 1

    print(f"The password is {password_count}")
    print(f"The dial passed 0 {n_passed_zero} times")
