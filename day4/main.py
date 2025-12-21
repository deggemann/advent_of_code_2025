from dataclasses import dataclass

def load_data(path):
    range_id = True
    range_ids = []
    items = []
    with open(path) as f:
        for line in f.readlines():
            if line == "\n":
                range_id = False
                continue

            if range_id:
                splitted_range = line.rstrip("\n").split("-")
                range_ids.append(Range(int(splitted_range[0]), int(splitted_range[1])))
            
            else:
                items.append(int(line.rstrip("\n")))


    return (range_ids, items)


class Comparer():
    def __init__(self, ranges):
        self.ranges = ranges
    
    def compare(self, item):
        for id_range in self.ranges:
            if id_range.in_range(item):
                return True
        
        return False

def recursive_check_range(ranges):
    # compare first range with each other range, if an update is made recursively call function.
    # Whenn all ranges are compared without update all the functions return the pruned range list
    for compared_range in ranges:
        for i, current_range in enumerate(ranges):
            upper_inside = compared_range.in_range(current_range.end)
            lower_inside = compared_range.in_range(current_range.start)

            if upper_inside and lower_inside:
                # range is unneaded
                print(f"{compared_range} already fully contain {current_range}")
                ranges.pop(i)
                return recursive_check_range(ranges)
            
            elif upper_inside:
                # remove current range and update lower range the compared one
                print(f"Upper end of {current_range} in {compared_range}")
                compared_range.start = current_range.start
                
                ranges.pop(i)
                return recursive_check_range(ranges)

            elif lower_inside:
                # remove current range and update upper range of compared one
                print(f"Lower end of {current_range} in {compared_range}")
                compared_range.end = current_range.end
                ranges.pop(i)
                return recursive_check_range(ranges)
    return ranges


@dataclass
class Range:
    start: int
    end: int

    def in_range(self, value):
        bigger = value > self.start
        smaller = value < self.end
        return bigger and smaller


if __name__ == "__main__":
    PATH = "day4/input.txt"
    range_ids, items = load_data(PATH)

    comparer = Comparer(range_ids)

    result = list(map(comparer.compare, items))

    print(f"Total items: {len(items)}")
    print(f"Total compared items: {len(result)}")
    print(f"Number of fresh ingredients: {sum(result)}")

    len_ranges = len(range_ids)
    pruned_ranges = recursive_check_range(range_ids)
    print(f"Number of ranges before pruning: {len_ranges}, after pruning: {len(pruned_ranges)}")

    print(pruned_ranges)


    total_items = 0
    for pruned_range in pruned_ranges:
        total_items += (pruned_range.end - pruned_range.start) + 1

    print(f"Total number of fresh items: {total_items}")





