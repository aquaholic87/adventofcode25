def main():
    banks = read_file() 
    banks = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    banks = ["234234234234278"]
    total = 0
    for bank in banks:
        result = highest_joltage(bank)
        total += result
        print(result)
    print(total)

def read_file():
    with open("day3.txt", "r") as file:
        content = file.read().splitlines()
    return content

def highest_joltage(bank):
    bank = [int(num) for num in bank]
    nums = []
    #index of bank needs to be relative to amount left in bank
    for i in range(12):
        nums.append(max(bank[:4-i]))
        bank = bank[bank.index(nums[-1])+1:]
    return int("".join([str(num) for num in nums]))


# def highest_joltage(bank):#FOR PART 1
#     bank = [int(number) for number in bank]
#     print(bank)
#     max1 = 0
#     max2 = 0
#     for i, num in enumerate(bank):
#         if num > max1 and i < len(bank) -1:
#             max1 = num
#             max2 = bank[i+1]
#         elif num > max2:
#             max2 = num
#     return int(str(max1) + str(max2))

if __name__ == "__main__":
    main()

