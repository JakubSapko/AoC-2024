import re

filename = "input.txt"


# mul\([0-9]{1,3},[0-9]{1,3]\)
def solve_part_one(data) -> int:
    proper_muls = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data, flags=0)
    numbers_of_muls = map(lambda x: re.findall(r"[0-9]{1,3}", x, flags=0), proper_muls)
    casted_numbers_of_muls = list(map(lambda x: (int(x[0]), int(x[1])), numbers_of_muls))
    res = sum(list(map(lambda mul: mul[0] * mul[1], casted_numbers_of_muls)))

    return res


# (mul|do|don't)\([0-9{1,3},[0-9]{1,3}\)
def solve_part_two(data) -> int:
    proper_muls = re.findall(r"(mul|do|don\'t)\((\d+,\d+|)\)", data)

    res = 0
    flag = True

    for match in proper_muls:
        op, args = match

        if op == "do":
            flag = True
        if op == "don't":
            flag = False
        if op == "mul" and flag:
            n1, n2 = args.split(",")
            res += int(n1) * int(n2)
    return res





if __name__ == "__main__":
    with open(filename) as input:
        input = input.read()
        p1 = solve_part_one(input)
        print(f"Part one: {p1}")
        p2 = solve_part_two(input)
        print(f"Part two: {p2}")
