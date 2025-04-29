hex_digits = "0123456789ABCDEF"
var_continue = "yes"
while var_continue in ["yes","y",""]:
    while True:
        try:
            base10 = input("Input a base 10 number:\n")
            base10 = base10.strip().replace(" ", "")
            divider = int(base10)
            if divider < 0:
                raise ValueError
            if divider == 0:
                hex_result = "0"
            else:
                hex_result = ""
                while divider > 0:
                    remainder = divider % 16
                    hex_digit = hex_digits[remainder]
                    hex_result = hex_digit + hex_result
                    divider = divider // 16
            break
        except ValueError:
            print("Please input a valid non-negative base 10 number.")
    print(hex_result)
    var_continue = input("Would you like to make another hex number? (Yes)(no):\n")
    while var_continue.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue = input("Would you like to convert another number? (Yes/No):\n")

var_continue2 = "yes"
while var_continue2 in ["yes","y",""]:
    while True:
        try:
            base16 = input("Input a hexadecimal number:\n").upper()
            base16 = base16.strip().replace(" ", "")
            if base16 == "" or not all(c in hex_digits for c in base16):
                raise ValueError("Invalid hex number")
            decimal = 0
            n = len(base16)
            for i in range(n):
                digit = base16[i]
                value = hex_digits.index(digit)
                power_of_16 = n - 1 - i
                decimal += value * (16 ** power_of_16)
            break
        except ValueError as e:
            print(f"Error: {e}. Please input a valid hex number.")
    print(decimal)
    var_continue2 = input("Would you like to make another hex number? (Yes)(no):\n")
    while var_continue2.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue2 = input("Would you like to convert another number? (Yes/No):\n")

