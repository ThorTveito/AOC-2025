maximumjoltage = 0

with open("test.txt", "r") as file:
    for line in file:
        digits = [int(d) for d in line.strip()]
        print(digits)
        maxjolt = ""
        print(maxjolt)

        while len(maxjolt) < 12:
            if len(digits) == 0:
                break
            
            tempMax = max(digits)
            print(tempMax)
            if len(digits[digits.index(tempMax):+1]) > 12 - len(maxjolt):
                maxjolt += str(tempMax)
                digits = digits[digits.index(tempMax)+1:]
            else:
                digits = digits[digits.index(tempMax)+1:]
            print(maxjolt)   
        # print(maxjolt)       
# print(maximumjoltage)