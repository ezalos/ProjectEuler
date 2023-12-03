import colorama

def day_1a():
    file_path = "data/test/day_1a.txt"
    nb_list = []
    with open(file_path) as f:
        for i, line in enumerate(f.readlines()):
            a = None
            b = None
            for c in line:
                if not c.isdigit():
                    continue
                if a is None:
                    a = int(c)
                b = int(c)
            if a is None or b is None:
                print(f"line {i}: {a = } & {b = }. {line = }")
            nb_list.append((a * 10) + b)
    print(f"{sum(nb_list) = }")


def day_1b():
    file_path = "data/example/day_1b.txt"
    file_path = "data/test/day_1b.txt"
    nb_list = []
    valid = {
        "one": 1,
        "1": 1,
        "two": 2,
        "2": 2,
        "three": 3,
        "3": 3,
        "four": 4,
        "4": 4,
        "five": 5,
        "5": 5,
        "six": 6,
        "6": 6,
        "seven": 7,
        "7": 7,
        "eight": 8,
        "8": 8,
        "nine": 9,
        "9": 9,
        "0": 0,
    }

    def is_fit(line):
        for k in valid.keys():
            if len(k) > len(line):
                continue
            if k == line[:len(k)]:
                return valid[k]
        return None

    with open(file_path) as f:
        for i, line in enumerate(f.readlines()):
            a = None
            b = None
            for i, c in enumerate(line):
                nb = is_fit(line[i:])
                if nb is None:
                    continue
                if a is None:
                    a = nb
                b = nb
            if a is None or b is None:
                print(f"line {i}: {a = } & {b = }. {line = }")
            nb_list.append((a * 10) + b)
    print(f"{sum(nb_list) = }")


def day_2a():
    file_path = "data/example/day_2a.txt"
    file_path = "data/test/day_2a.txt"
    games = {}
    with open(file_path) as f:
        for i, line in enumerate(f.readlines()):
            game, draws = line.split(":")
            game_id = int(game.split(" ")[1])
            l_draws = draws.split(";")
            games[game_id] = []
            for draw in l_draws:
                colors = draw.split(",")
                d = {}
                for c in colors:
                    nb, color = c.strip().split(" ")
                    d[color] = d.get(color, 0) + int(nb)
                # print(f"{d = }   {line = }")
                games[game_id].append(d)
    truth = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    print(f"{games = }")
    print(f"{truth = }")
    id_sum = 0
    for game_id, g_draws in games.items():
        error = False
        for draw_id, draws in enumerate(g_draws):
            for color in draws.keys():
                # print(f"{game_id = } {color = } {color in truth_list = }")
                # if color not in truth.keys():
                #     print(f"{game_id = } was impossible")
                #     error = True
                #     break
                if draws[color] > truth[color]:
                    # print(f"{game_id = } was impossible")
                    # print(f"{draw_id = } {color = }")
                    # print(f"\t{draws[color] = }")
                    # print(f"\t{truth[color] = }")
                    # print(f"{draws= }")
                    error = True
                    break
            if error:
                break
        if not error:
            id_sum += game_id
    print(f"{id_sum}")

def day_2b():
    file_path = "data/example/day_2a.txt"
    file_path = "data/test/day_2a.txt"
    games = {}
    with open(file_path) as f:
        for i, line in enumerate(f.readlines()):
            game, draws = line.split(":")
            game_id = int(game.split(" ")[1])
            l_draws = draws.split(";")
            games[game_id] = []
            for draw in l_draws:
                colors = draw.split(",")
                d = {}
                for c in colors:
                    nb, color = c.strip().split(" ")
                    d[color] = d.get(color, 0) + int(nb)
                games[game_id].append(d)
    power_of_sets = []
    for game_id, g_draws in games.items():
        minimum_set = {}
        for draw_id, draws in enumerate(g_draws):
            for color, quantity in draws.items():
                if minimum_set.get(color, 0) < quantity:
                    minimum_set[color] = quantity
            power_of_set = 1
        for q in minimum_set.values():
            power_of_set *= q
        print(f"{game_id = } {power_of_set = }")
        power_of_sets.append(power_of_set)
    print(f"{sum(power_of_sets)}")


def day_3a():
    file_path = "data/example/day_3a.txt"
    file_path = "data/test/day_3a.txt"
    with open(file_path) as f:
        engine_schematic = f.readlines()
    part_numbers = 0
    def check_around(row_id, cold_id):
        pairs = [
            (row_id - 1, cold_id - 1),
            (row_id - 1, cold_id),
            (row_id - 1, cold_id + 1),
            (row_id, cold_id - 1),
            (row_id, cold_id),
            (row_id, cold_id + 1),
            (row_id + 1, cold_id - 1),
            (row_id + 1, cold_id),
            (row_id + 1, cold_id + 1),
        ]
        for r, c in pairs:
            # print(f"{r, c = }")
            if not 0 <= r < len(engine_schematic):
                # print(f"bad r")
                continue
            if not 0 <= c < len(engine_schematic[row_id]):
                # print(f"bad c")
                continue
            x = engine_schematic[r][c]
            # print(f"{x = }")
            if x.isdigit():
                # print(f"Bad digit")
                continue
            if x == "." or x == "\n":
                # print(f"Bad .")
                continue
            # print(f"Good !")
            print(f"True for {r, c = } {x = } for {row_id, cold_id = } {engine_schematic[row_id][col_id]}")
            return True
        return False

    a = colorama.Fore.RED
    b = colorama.Fore.BLUE
    c = colorama.Fore.GREEN
    d = colorama.Fore.RESET
    ls = []
    for row_id, row in enumerate(engine_schematic):
        number_begin = None
        part_number = None
        is_adjacent = False
        l = ""
        for col_id, col in enumerate(row):
            x = engine_schematic[row_id][col_id]
            if col.isdigit():
                l += a
                if number_begin is None:
                    number_begin = col_id
            # elif number_begin is not None and part_number is not None:
                # while not row[col_id - 1].isdigit():
                #     col_id -= 1
                # part_number = int(row[number_begin:col_id])
            if number_begin is not None and not is_adjacent:
                is_adjacent = check_around(row_id, col_id)
                if is_adjacent:
                    l += c
            if not col.isdigit() and col != "\n":
                l += b
                if is_adjacent:
                    # if part_number is None:
                    while not row[col_id - 1].isdigit():
                        col_id -= 1
                    part_number = int(row[number_begin:col_id])
                    part_numbers += part_number
                    print(f"ADJ {part_number = }")
                elif number_begin:
                    print(f"NOT {part_number = }")
                number_begin = None
                is_adjacent = False
                part_number = None
            l += x + d
        ls.append(l)
        # break
    for l in ls:
        print(l)
    print(f"{part_numbers = }")

# 528131 is too high


def launch_day():
    fn = day_3a
    solution = fn()
    return solution
