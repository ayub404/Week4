def decimal_to_binary(n):
    if n == 0:
        return '0'
    
    binary = ''
    while n > 0:

        
        reminder = n % 2
        n = n // 2
        binary = str(reminder) + binary
    return binary



def binary_to_decimal(binary_str):
    binary_str = str(binary_str)
    decimal = 0
    pow = len(str(binary_str)) - 1
    for i in str(binary_str):
        decimal +=  (2 ** pow) * int(i) 
        pow -= 1
    return decimal
        
   

# print(binary_to_decimal(10))


def decimal_to_hex_digit(n):
    hex_dig = ''
    if n == 0:
        return '0'
    while n > 0:
        reminder = n % 16

        n = n // 16
    
        if reminder == 10:
            hex_char = 'A'
        elif reminder == 11:
            hex_char = 'B'
        elif reminder == 12:
            hex_char = 'C'
        elif reminder == 13:
            hex_char = 'D'
        elif reminder == 14:
            hex_char = 'E'
        elif reminder == 15:
            hex_char = 'F'
        else:
            hex_char = str(reminder) 
        
    
        hex_dig = hex_char + hex_dig
        
            
    return hex_dig


def is_valid_binary(binary_str):
    for dig in str(binary_str):
        if dig != '0' and dig != '1':
            return False
    return True

def count_ones_in_binary(binary_str):
    count = 0
    for digit in str(binary_str):
        if digit != '1' and digit != '0':
            return False
    for dig in str(binary_str):
        if dig == '1':
            count += 1
    return count

# dec_tibin  = decimal_to_binary(25) 
# print(f"Decimal '25' to binary: {dec_tibin}")
# print(f"Binary '11011' to decimal: ")


print('\nNumber System Converter')
print('-' * 40)
decimal = decimal_to_binary(25)
binary = binary_to_decimal(11011)
print(f"Decimal 25 to binary: {decimal}")
print(f"Binary 11011 to decimal: {binary}\n")
print(f"Is '1010' valid binary? {is_valid_binary(1010)}")
print(f"Is '1012' valid binary? {is_valid_binary(1012)}")
print(f"Is '1111' valid binary? {is_valid_binary(1111)}\n")

print(f"Number of 1s in '110101': {count_ones_in_binary(110101)}\n")

print(f"Decimal 9 to hex: {decimal_to_hex_digit(9)}")
print(f"Decimal 10 to hex: {decimal_to_hex_digit(10)}")
print(f"Decimal 15 to hex: {decimal_to_hex_digit(15)}")



