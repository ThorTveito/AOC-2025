invalidIds = 0


with open("input.txt", "r") as file:
    line = file.readline()
    lines = line.strip().split(",")
    for ids in lines:
        idRange = ids.split("-")
        for i in range(int(idRange[0]), int(idRange[1])+1):
            istr = str(i)
            tempStr = ""
            
            for character in istr:
                tempStr += character
                if((len(istr) // len(tempStr)) >= 2 and (len(istr)//len(tempStr))*tempStr == istr):
                    print("****************************")
                    invalidIds += i
                    break
                
print(invalidIds)