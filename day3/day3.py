maximumjoltage = 0

with open("input.txt", "r") as file:
    for line in file:
        largest = 0
        secondLargest = 0
        digits = [int(d) for d in line.strip()]
        for i, digit in enumerate(digits):
            largest = max(digits[:len(digits)-1])
            secondLargest = max(digits[digits.index(largest)+1:])
        print(largest, secondLargest)
        maximumjoltage += int(str(largest) + str(secondLargest))
        
print(maximumjoltage)