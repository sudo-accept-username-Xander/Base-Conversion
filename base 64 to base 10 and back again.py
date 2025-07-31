base64_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
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
                base_64 = "A"
            else:
                base_64 = ""
                while divider > 0:
                    remainder = divider % 64
                    base64_digit = base64_digits[remainder]
                    base_64 = base64_digit + base_64
                    divider = divider // 64
            break
        except ValueError:
            print("Please input a valid non-negative base 10 number.")
    print(base_64)
    var_continue = input("Would you like to make another base64 number? (Yes)(no):\n")
    while var_continue.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue = input("Would you like to convert another number? (Yes/No):\n")

var_continue2 = "yes"
while var_continue2 in ["yes","y",""]:
    while True:
        try:
            base64 = input("Input a base64 number:\n")
            base64 = base64.strip().replace(" ", "")
            if base64 == "" or not all(c in base64_digits for c in base64):
                raise ValueError("Invalid base64 number")
            decimal = 0
            n = len(base64)
            for i in range(n):
                digit = base64[i]
                value = base64_digits.index(digit)
                power_of_64 = n - 1 - i
                decimal += value * (64 ** power_of_64)
            break
        except ValueError as e:
            print(f"Error: {e}. Please input a valid base64 number.")
    print(decimal)
    var_continue2 = input("Would you like to make another base64 number? (Yes)(no):\n")
    while var_continue2.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue2 = input("Would you like to convert another number? (Yes/No):\n")

