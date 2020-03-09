code_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,  'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15}
code_table_reverse = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def convert(number, basisIn, basisOut):
    value = 0
    number = str(number)
    # calculating  the value in the decimal system
    for i in range(1, len(number)+1):
        value += code_table[(number)[-i]]*basisIn**(i-1)
    
    # calculating length of the number saved to the new system
    length = 0
    while basisOut**length < value:
        length += 1
    
    output = ''

    # main converting
    if basisOut**(length-1)*basisOut == value:
        output += code_table_reverse[1]
        for i in range(length):
            output += code_table_reverse[0]
        return output
    
    else:
        for i in range(length - 1, -1, -1):
            asigned = False
            for j in range(0, basisOut+1):
                if asigned == True:
                    continue
                if basisOut**i*j > value:
                    if j == 0:
                        output += code_table_reverse[j]
                        asigned = True
                    else:
                        output += code_table_reverse[j-1]
                        value -= basisOut**i*(j-1)
                        asigned = True
        return output
number = input("Which number do you want to convert?: ")
base = int(input("Tell me the base of the system: e.g (2,10,16): "))

print("  BINARY      |  OCTAL       |  DECIMAL     |  HEXADECIMAL ")
print("------------------------------------------------------------")
print(convert(number, base, 2) +"         " + convert(number, base, 8)+"         " + convert(number, base, 10)+"         " + convert(number, base, 16))

