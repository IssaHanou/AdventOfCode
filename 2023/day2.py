def part1(file):
    with open(file) as f:
        cubes = {"red": 12, "blue": 14, "green": 13}
        all_ids = set()
        bad_ids = set()
        for line in f:
            game, sets = line.split(": ")
            game = int(game.split(" ")[1])
            all_ids.add(game)
            sets = sets.strip().split("; ")
            for s in sets:
                blocks = s.split(", ")
                for color in blocks:
                    n, c = color.split(" ")
                    if int(n) > cubes[c]:
                        bad_ids.add(game)
        print(sum(all_ids.difference(bad_ids)))


def part2(file):
    with open(file) as f:
        cubes = {"red": 12, "blue": 14, "green": 13}
        powers = []
        for line in f:
            game, sets = line.split(": ")
            game = int(game.split(" ")[1])
            sets = sets.strip().split("; ")
            cubes = {"red": 0, "blue": 0, "green": 0}
            for s in sets:
                blocks = s.split(", ")
                for color in blocks:
                    n, c = color.split(" ")
                    if int(n) > cubes[c]:
                        cubes[c] = int(n)
            powers.append(cubes["red"] * cubes["blue"] * cubes["green"])
        print(sum(powers))
if __name__ == "__main__":
    part2("day2.txt")