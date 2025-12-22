def main():
    towels, result = read_file('day4.txt'), read_file('day4.txt')
    # towels, result = test_case(), test_case()
    counts = []
    while True:

        new_count, result = remove_towel(0, 0, towels, result)
        towels = result
        counts.append(new_count)
        if new_count == 0:
            break


    print(sum(counts))    



def remove_towel(row, col, towels, result):

    count = 0
    for r in range(len(towels)):
        for c in range(len(towels[0])):
            if towels[r][c] == "@":
                adjacent = towels_adjacent(r, c, towels)
                if adjacent < 4:
                    count +=1
                    result[r][c] = "."
    return count, result

def read_file(filename):
    with open(filename, 'r') as file:
        towels = file.read().splitlines()
    towels = [list(towel) for towel in towels]
    return towels

def test_case():
    x = ["..@@.@@@@.", "@@@.@.@.@@", "@@@@@.@.@@", "@.@@@@..@.", "@@.@@@@.@@",
            ".@@@@@@@.@", ".@.@.@.@@@", "@.@@@.@@@@", ".@@@@@@@@.", "@.@.@@@.@."]
    x = [list(towel) for towel in x]
    return x

def towels_adjacent(row, col, towels):
    adjacent = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            r_temp, c_temp = row + i, col + j
            if 0 <= r_temp < len(towels) and 0 <= c_temp < len(towels[0]):
                if towels[r_temp][c_temp] == "@":
                    adjacent += 1

    return adjacent
    


if __name__ == "__main__":

    main()

