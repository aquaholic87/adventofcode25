def main():
    banks = read_file() 
    # banks = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    # banks = [banks[:]]
    # banks = ["8666467466748463644436358474464684357755754832476479449554745556415435374495644765744447544234798447",
    #          "2335242224342412391423234223574342632221234413244136124423434433531252523312322433224322224222243422",
    #          "1333332334833332432232224334393373323336233244233224333373332433113231332432333333423134322352433433"]
    # banks = [banks[0]]
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
    leeway = len(bank) - 12 + 1

    for i in range(12):
        nums.append(max(bank[:leeway]))
        leeway -= bank.index(nums[i])
        bank = bank[bank.index(nums[i])+1:]
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

