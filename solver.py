dial = 50
password = 0

with open("input.txt", "r") as file:
    for line in file:
        prev_dial = dial
        print(f"Start: {dial}")
        direction = line[0]
        number = int(line[1:])  
        print(f"Increase: {number//100}")
        password += number // 100
        print(f"Number: {direction} {number}")
        number = number % 100
        
        if direction == "R":
            prev_dial = dial
            dial = (dial + number) % 100 
            if (dial < prev_dial) and (dial != 0):
                password += 1
            
        if direction == "L":
            dial = dial - number
            if dial < 0:
                if(prev_dial != 0):
                    password += 1
                dial = 100 + dial   
        
        print(f"Slutt: {dial}")
        if(dial == 0):
            password += 1
            
print(password)