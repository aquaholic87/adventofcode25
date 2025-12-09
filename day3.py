def main():
    banks = read_file() 
    banks = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    total = 0
    for bank in banks:
        result = highest_joltage(bank)
        total += result
        print(result)

def read_file():
    with open("day3.txt", "r") as file:
        content = file.read().splitlines()
    return content

def highest_joltage(bank):
    bank = bank.split()
    max1 = bank[0]
    max2 = bank[1]
    for i, num in enumerate(bank):
        if i > len(bank):
            break
        if int(num) > max1:
            max1 = num
        elif int(num) > max2:
            max2 = num
    return int(max1) * int(max2)

if __name__ == "__main__":
    main()