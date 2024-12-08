
filename = "input.txt"


def is_monotonic_by_one_to_three(lst: list[int]) -> bool:
    if len(lst) <= 1:
        return True
    increasing = all((lst[i] <= lst[i+1]) and (lst[i+1] - lst[i] >= 1 and lst[i+1] - lst[i] <= 3) for i in range(len(lst) - 1))
    decreasing = all((lst[i] >= lst[i+1]) and (lst[i] - lst[i + 1] >= 1 and lst[i] - lst[i + 1] <= 3) for i in range(len(lst) - 1))
    return increasing or decreasing


def is_monotonic_by_one_to_three_with_problem_dampener(lst: list[int]) -> bool:
    n = len(lst)
    candidates = [lst for _ in range(n)]

    candidates_skipped = [candidates[:i] + candidates[i+1:] for i, candidates in enumerate(candidates)]

    return any(map(is_monotonic_by_one_to_three, candidates_skipped))



if __name__ == "__main__":
    safe_counter = 0
    almost_safe_counter = 0
    with open(filename) as file:
        for line in file:
            line_parsed: list[int] = [int(x) for x in line.split(" ")]
            if is_monotonic_by_one_to_three(line_parsed):
                safe_counter += 1
            if is_monotonic_by_one_to_three_with_problem_dampener(line_parsed):
                almost_safe_counter += 1
    print(f"Safe counter:  {safe_counter}")
    print(f"Almost safe counter: {almost_safe_counter}")
