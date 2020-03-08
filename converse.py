""" print("siema")
basis = 10
number_decimal = 0
print("1 --- dwojkowy")
print("2 --- osemkowy")
print("3 --- dziesietny")
print("4 --- szesnastkowy")
a = input("Podaj system kodowania liczby: ")
number = input("Podaj liczbe: ")
 
print(number[-1])
print(len(number))
if a == '1':
    basis = 2
elif a == '2':
    basis = 8
elif a == '3':
    basis = 10
elif a == '4':
    basis = 16
print(basis)
#if basis == 2:
 #   number_binary = number
#    number_decimal
for i in range(1,len(number)+1):
    number_decimal += int(number[-i])*basis**(i-1)
print("Liczba dziesietnie wynosi: " + str(number_decimal)) """
 
code_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '9': 8, 'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15}
code_table_reverse = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
def convert(number, basisIn, basisOut):
    value = 0
    number = str(number)
    for i in range(1, len(number)+1):
        value += code_table[(number)[-i]]*basisIn**(i-1)
    print(value)
    length = 0
    while basisOut**length < value:
        length += 1
    print(length)
    for i in range(1, basisOut):
        print(i)
convert(92, 16, 4)

print(code_table['e'])