
filename = "input.txt"

def is_monotonic_by_one_to_three(lst: list[int]) -> bool:
    if len(lst) <= 1:
        return True
    increasing = all((lst[i] <= lst[i+1]) and (lst[i+1] - lst[i] >= 1 and lst[i+1] - lst[i] <= 3) for i in range(len(lst) - 1))
    decreasing = all((lst[i] >= lst[i+1]) and (lst[i] - lst[i + 1] >= 1 and lst[i] - lst[i + 1] <= 3) for i in range(len(lst) - 1))
    return increasing or decreasing

if __name__ == "__main__":
    safe_counter = 0
    with open(filename) as file:
        for line in file:
            line_parsed: list[int] = [int(x) for x in line.split(" ")]
            if is_monotonic_by_one_to_three(line_parsed):
                safe_counter += 1
    print(f"Safe counter:  {safe_counter}")
