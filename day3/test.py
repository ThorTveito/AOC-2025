maximumjoltage = 0

with open("test.txt", "r") as file:
    for line in file:
        digits = [int(d) for d in line.strip()]
        maxjolt = ""

        while len(maxjolt) < 12 and len(digits) > 0:
            tempMax = max(digits)
            maxjolt += str(tempMax)
            digits = digits[digits.index(tempMax)+1:]
            
        print(maxjolt)
        maximumjoltage += int(maxjolt)
        
print(maximumjoltage)