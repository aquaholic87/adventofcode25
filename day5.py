def main1():
    idranges, ids = get_data()
    valid_ranges = calc_valids(idranges)
    count = 0
    for id in ids:
        for valid_range in valid_ranges:
            if valid_range[0] <= int(id) <= valid_range[1]:
                count += 1
                break
    print(count)

def main2():
    idranges, ids = get_data()
    valid_ranges = calc_valids(idranges)
    valid_ranges.sort()

    valid_ranges_merged = []
    current_start, current_end = valid_ranges[0]
    for vr in valid_ranges[1:]:
        if vr[0] <= current_end + 1:
            current_end = max(current_end, vr[1])
        else:
            valid_ranges_merged.append([current_start, current_end])
            current_start, current_end = vr
    valid_ranges_merged.append([current_start, current_end])
    count = 0
    for vr in valid_ranges_merged:
        count += vr[1] - vr[0] + 1
    print(count)

def get_data():
    with open('day5.txt', 'r') as file:
        data = file.read().splitlines()
    

    id_ranges = data[:data.index("")]
    ids = data[data.index("")+1:]
    return id_ranges, ids

def calc_valids(idranges):
    valids = []
    for idrange in idranges:
        parts = idrange.split("-")
        start, end = int(parts[0]), int(parts[1])
        valids.append([int(start), int(end)])
    return valids

if __name__ == "__main__":
    main2()