def main():
    instructions = read_file("day1.txt")
    #instructions = ["L68","L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82", "R1000"]
    #instructions = ["R1000"]
    count = 0
    value = 50
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1:])
        
        # Check if we cross zero during this move
        if direction == "R":
            for i in range(1, amount + 1):
                value += 1
                value = value % 100
                if value == 0:
                    count += 1
        elif direction == "L":
            for i in range(1, amount + 1):
                value -= 1
                value = value % 100
                if value == 0:
                    count += 1
    print("Final value:", value)
    print("Count of zeros:", count)

def read_file(file_path):#returns list of instructions.
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data



if __name__ == "__main__":
    main()
    
# #PART 1
# def main():
#     instructions = read_file("day1.txt")
#     #TEST: instructions = ["L68","L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82" ]
#     count = 0
#     value = 50
#     for instruction in instructions:
#         direction = instruction[0]
#         amount = int(instruction[1:])
#         if direction == "R":
#             value = (value + amount) % 100

#         elif direction == "L":
#             value = (value - amount) % 100
#         if value == 0:
#             count += 1 
#     print("Final value:", value)
#     print("Count of zeros:", count)
