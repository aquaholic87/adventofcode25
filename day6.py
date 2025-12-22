import numpy as np

def main():
    data = import_data()
    
    results = list()

    for line in data:
        operator = line[-1]
        
            
        if operator == "+":
            results.append(int(line[0]) + int(line[1]) + int(line[2]) + int(line[3]))
        else:
            results.append(int(line[0]) * int(line[1]) * int(line[2]) * int(line[3]))

        print("Line:", line, "Operator:", operator, "Result:", results[-1])
    
    print("Results:", results)
    print("Sum of results:", sum(results))

def import_data():



    with open('day6.txt', 'r') as file:
        data = file.read().splitlines()
    

    print("Raw data:", data )

    x = [line.split() for line in data ]

    processsed = []

    for line in x:
        print(type(line))
        processsed.append([item for item in line if item != ""])

    flipped = np.array(processsed).T.tolist()

    print("Processed data:", processsed)
    print("Flipped data:", flipped)


    return flipped

def import_data2():
    with open('day6.txt', 'r') as file:
        data = file.read().splitlines()
    data = [line.split(" ") for line in data ]
    print("Raw data:", data )
    
if __name__ == "__main__":
    import_data2()
    exit()
    main()