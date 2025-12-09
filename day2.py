def main():
    with open("day2.txt", 'r') as file:
        IDs = file.read()
    # IDs = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    IDs = IDs.split(',')
    invalid = 0
    invalid_IDs = []
    for ID_chunk in IDs:
        min_val, max_val = min_max(ID_chunk)
        for ID in range(min_val, max_val + 1):
            ID = str(ID)
            if not is_valid(ID):
                invalid += 1
                invalid_IDs.append(int(ID))
    print("Invalid IDs:", invalid_IDs)
    print(sum(invalid_IDs))

            

    print("Number of invalid IDs:", invalid)
    print(sum(invalid_IDs))

def min_max(ID):#returns min and max values from ID string
    dash = ID.index('-')
    min_val = int(ID[:dash])
    max_val = int(ID[dash + 1:])
    return min_val, max_val

def find_factors(n):#returns list of factors of n
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def is_valid(ID: str) -> bool:#returns True if ID is valid, False otherwise
    length = len(ID)
    factors_of_length = find_factors(length)[:-1]#exlude last one which is the length
    for factor in factors_of_length:
        if ID[:factor] * int(length // factor) == ID:
            return False
    return True
        
if __name__ == "__main__":
    main()


def main1():#for part one
    with open("day2.txt", 'r') as file:
        IDs = file.read()
    # IDs = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    IDs = IDs.split(',')
    invalid = 0
    invalid_IDs = []
    for ID in IDs:
        min_val, max_val = min_max(ID)
        for i in range(min_val, max_val + 1):
            i = str(i)
            if len(i) % 2 == 0:
                if i[0:len(i)//2] == i[len(i)//2:]:
                    invalid += 1
                    invalid_IDs.append(int(i))
            else:
                print("Odd length ID:", i)
    print("Number of invalid IDs:", invalid)
    print(sum(invalid_IDs))