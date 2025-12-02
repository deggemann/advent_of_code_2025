
def load_data(path) -> list:
    with open(path) as f:
        ids = f.readline()
    ids = ids.split(",")
    return ids

def check_odd_number_digit(id_range: str) -> bool:
    """
    return if any invalid id present in the range.
    If start and end of the range have the same number of digits (odd)
    then there can not be a sequence of digits repeated exactly twice
    """
    is_odd = False
    list_id_range = id_range.split("-")

    if (len(list_id_range[0]) == len(list_id_range[1])) and len(list_id_range[0]) % 2 == 1:
        print(f"Range with only odd digits found: {id_range}, skipping it entirely")
        is_odd = True

    return False

def check_repetition(number: str) -> bool:
    repetition = False
    if len(number) % 2 == 1:
        return False

    
    middle = int(len(number)/2)

    if number[:middle] == number[middle:]:
        repetition = True

    return repetition

def check_true_repetition(number: str) -> bool:
    """
    for second part of the puzzle.
    Any number of digit reptetitions is valid. E.g. 111, 121212 123123
    """
    for n_digit in range(1, len(number)//2 + 1):
        split = number.split(number[:n_digit]) # if repetition will return list with empty string: ["", "", ""]
        if "".join(split) == '':
            return True

    return False

     

if __name__ == "__main__":
    PATH = "input.txt"
    ids_list = load_data(PATH)

    id_with_simple_repetition = []
    id_with_true_repetition = []

    # part one of the puzzle
    for ids in ids_list:
        if check_odd_number_digit(ids):
            continue
        
        ids_range = ids.split("-")

        for i in range(int(ids_range[0]), int(ids_range[1]), 1):
            if check_repetition(str(i)):
                print(f"Number with repetition found: {i}")
                id_with_simple_repetition.append(i)


    # part two of the puzzle
    for ids in ids_list:    
        ids_range = ids.split("-")

        for i in range(int(ids_range[0]), int(ids_range[1]), 1):
            if check_true_repetition(str(i)):
                print(f"Number with repetition found: {i}")
                id_with_true_repetition.append(i)


    print(f"Sum of all ids with simple repeating pattern is: {sum(id_with_simple_repetition)}")
    print(f"Sum of all ids with True repeating pattern is: {sum(id_with_true_repetition)}")
