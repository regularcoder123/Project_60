binary_num = input("Enter your Binary number here:")

decimal_num = 0

for digit in binary_num:
    decimal_num = decimal_num * 2 + int(digit)

print(f"Decimal Number: {decimal_num}")