import math
def menu():
    print("""Convert...
1. Binary to Denary
2. Denary to Binary
3. Hex to Denary
4. Denary to Hex
5. Binary to Hex
6. Hex to Binary
7. 2s Complement to Denary
8. Denary to 2s Complement
9. Denary to Fixed Point Binary
10. Fixed Point Binary to Denary
11. Denary to Floating Point Binary
12. Floating Point Binary to Denary""")
    
    menuChoice = userInput("Please enter your menu choice: ")
    return menuChoice

def userInput(message):
    userResponse = input(message)
    return userResponse

#--------------------------------------------------------------------------------------------------------------------------
#      BINARY TO DENARY


def b2d():
    byte = input("Please enter a binary value:")
    counter = len(byte)  #sets the counter to the length of the byte integer
    denary = 0 #sets denary to 0
    for bit in byte: #iterate over each bit in the byte
        if bit == "1": #if the current bit = 1 do:
            denary +=  2**counter  #setting denary to 2^the counter working out the current bits value
        counter -= 1  #counter = counter - 1
    denary = math.floor(denary / 2)
    return denary  #returns the denary string


#--------------------------------------------------------------------------------------------------------------------------
#      DENARY TO BINARY


def d2b():
    denNum = input("Please enter a denary number up to 255")
    Binary = ''                 #creating a blank output string
    product = int(denNum)     #setting the "product" of the loop to the same as the input so it can iterate over it
    while len(Binary) < 8:    #while loop to run until the binary output is 8 digits long
        currentBin = product % 2   #sets the current binary digit to the remainder of prod / 2
        product = math.floor(product / 2)  #dividing prod by 2, rounding down and setting it to itself
        Binary = str(currentBin) + Binary   #concatenate the current binary number onto the front of the binary output
    return Binary    #returns the binary string


#--------------------------------------------------------------------------------------------------------------------------
#      HEX TO DENARY


def h2d():
    hexNum = input("Please enter a hex number up to 255")
    counter = 0
    denary = 0
    for digit in reversed(hexNum):   #iterates through hexNum backwards
        try:
            digit = digit.upper()
        except:
            pass
        if digit == "A":   #converts letters on hex to decimal values
            digit = 10
        elif digit == "B":
            digit = 11
        elif digit == "C":
            digit = 12
        elif digit == "D":
            digit = 13
        elif digit == "E":
            digit = 14
        elif digit == "F":
            digit = 15
        currentDen = int(digit) * 16**counter  #carries out the operation <digit> * 16^<counter> to calculate the decimal value of <digit>
        counter += 1  #adds 1 to counter
        denary += currentDen #adds the current denary to the final denary output
    return denary  #returns the denary output


#--------------------------------------------------------------------------------------------------------------------------
#      DENARY TO HEX


def d2h():
    denNum = input("Please enter a denary number")
    hexa = ''
    prod = int(denNum)
    while prod > 0:  #loop to run while the value of prod is greater than 0 (run until divisions all return 0)
        remainder = prod % 16  #getting the remainder of the current value when divided by 16
        if remainder == 10:  #converting decimal hex values to letters
            remainder = "A"
        elif remainder == 11:
            remainder = "B"
        elif remainder == 12:
            remainder = "C"
        elif remainder == 13:
            remainder = "D"
        elif remainder == 14:
            remainder = "E"
        elif remainder == 15:
            remainder = "F"
        prod = math.floor(prod / 16)  #dividing prod (current value) by 16 ready for next iteration
        hexa = str(remainder) + hexa  #concatenating the remainder of the current calculation to the output variable
    return hexa


#--------------------------------------------------------------------------------------------------------------------------   
#      BINARY TO HEX


def b2h():
    byte = input("Please enter a binary value:")
    counter = len(byte)  #sets the counter to the length of the byte integer
    denary = 0 #sets denary to 0
    for bit in byte: #iterate over each bit in the byte
        if bit == "1": #if the current bit = 1 do:
            denary +=  2**counter  #setting denary to 2^the counter working out the current bits value
        counter -= 1  #counter = counter - 1
    denary = math.floor(denary / 2)
    hexa = ''
    prod = int(denary)
    while prod > 0:  #loop to run while the value of prod is greater than 0 (run until divisions all return 0)
        remainder = prod % 16  #getting the remainder of the current value when divided by 16
        if remainder == 10:  #converting decimal hex values to letters
            remainder = "A"
        elif remainder == 11:
            remainder = "B"
        elif remainder == 12:
            remainder = "C"
        elif remainder == 13:
            remainder = "D"
        elif remainder == 14:
            remainder = "E"
        elif remainder == 15:
            remainder = "F"
        prod = math.floor(prod / 16)  #dividing prod (current value) by 16 ready for next iteration
        hexa = str(remainder) + hexa  #concatenating the remainder of the current calculation to the output variable
    return hexa


#--------------------------------------------------------------------------------------------------------------------------
#      HEX TO BINARY


def h2b():
    hexNum = input("Please enter a hex number up to 255")
    counter = 0
    denary = 0
    for digit in reversed(hexNum):  #iterates through hexNum backwards
        try:
            digit = digit.upper()
        except:
            pass
        if digit == "A":   #converts letters on hex to decimal values
            digit = 10
        elif digit == "B":
            digit = 11
        elif digit == "C":
            digit = 12
        elif digit == "D":
            digit = 13
        elif digit == "E":
            digit = 14
        elif digit == "F":
            digit = 15
        currentDen = int(digit) * 16**counter  #carries out the operation <digit> * 16^<counter> to calculate the decimal value of <digit>
        counter += 1  #adds 1 to counter
        denary += currentDen #adds the current denary to the final denary output
    Binary = ''                 #creating a blank output string
    prod = int(denary)     #setting the "product" of the loop to the same as the input so it can iterate over it
    while len(Binary) < 8:    #while loop to run until the binary output is 8 digits long
        currentBin = prod % 2   #sets the current binary digit to the remainder of prod / 2
        prod = math.floor(prod / 2)  #dividing prod by 2, rounding down and setting it to itself
        Binary = str(currentBin) + Binary   #concatenate the current binary number onto the front of the binary output
    return Binary    #returns the binary string


#--------------------------------------------------------------------------------------------------------------------------    
#      2S COMPLEMENT TO DENARY


def c2d():
        Binary = input("please enter a 2s complement binary number:")
        Count = 7
        denary = 0
        for char in Binary:
            if (Count < 7):
                denary += denary + (2**(Count) * int(char))
            Count -= 1
        if Binary[0] == "1":
            denary = denary - 128
        return denary


    
#--------------------------------------------------------------------------------------------------------------------------       
#     DENARY TO 2S COMPLEMENT


def d2c():
    denNum = input("Please enter a denary number up to 127 and down to -128")
    Binary = ''
    nFlag = 0
    if denNum[0] == "-":
        nFlag = 1
        denNum = denNum.lstrip('-')
        print("denNum:",denNum)
        print("nFlag:",nFlag)               #creating a blank output string
    product = int(denNum)     #setting the "product" of the loop to the same as the input so it can iterate over it
    while len(Binary) < 7:    #while loop to run until the binary output is 8 digits long
        currentBin = product % 2   #sets the current binary digit to the remainder of prod / 2
        product = math.floor(product / 2)  #dividing prod by 2, rounding down and setting it to itself
        Binary = str(currentBin) + Binary   #concatenate the current binary number onto the front of the binary output
    Binary = str(nFlag) + Binary   
    return Binary    #returns the binary string
    
        



    
selection = menu()

if selection == "1":
    response = b2d()
    print(response)
elif selection == "2":
    response = d2b()
    print(response)
elif selection == "3":
    response = h2d()
    print(response)
elif selection == "4":
    response = d2h()
    print(response)
elif selection == "5":
    response = b2h()
    print(response)
elif selection == "6":
    response = h2b()
    print(response)
elif selection == "7":
    response = c2d()
    print(response)
elif selection == "8":
    response = d2c()
    print(response)
