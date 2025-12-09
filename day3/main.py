import numpy as np
from scipy import signal

def load_data(path):
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    list_rolls = []
    for line in lines:
        array = [0 if char == "." else 1 for char in line]
        list_rolls.append(array)

    return list_rolls

def get_removable_rolls(array):

    kernel = np.ones((3,3))
    kernel[1][1] = 0

    convolution = signal.convolve2d(array, kernel, mode="same", boundary="fill", fillvalue=0)
    mask = np.logical_not(array)
    roll_map_masked = np.ma.array(convolution, mask=mask, fill_value=0)


    roll_map = roll_map_masked.filled(0)
    limit = np.ones((np.shape(roll_map)))*4
    
    result = np.logical_and(np.less(roll_map, limit), np.invert(mask))

    return result


if __name__ == "__main__":
    PATH = "day3/input.txt"
    lines = load_data(PATH)

    array = np.array(lines)
    
    tot_rolls = np.sum(array)
    print(f"Total number of rolls is {tot_rolls}")
    removable_rolls = get_removable_rolls(array)
    
    count = 1
    while removable_rolls.any():
        removable_rolls = get_removable_rolls(array)

        new_array = np.ma.array(array, mask=removable_rolls, fill_value=0)

        array = new_array.filled(0)

        print(f"After {count} step the array looks like this: \n {array[:10,:10]}")
        count += 1

    
    final_rolls = np.sum(array)

    print(f"A total of {tot_rolls-final_rolls} were removed")
    print(f"{final_rolls} are unmovable")


