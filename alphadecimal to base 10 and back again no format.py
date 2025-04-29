alphadecimal_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
                alphadecimal = "0"
            else:
                alphadecimal = ""
                while divider > 0:
                    remainder = divider % 36
                    alphadecimal_digit = alphadecimal_digits[remainder]
                    alphadecimal = alphadecimal_digit + alphadecimal
                    divider = divider // 36
            break
        except ValueError:
            print("Please input a valid non-negative base 10 number.")
    print(alphadecimal)
    var_continue = input("Would you like to make another alphadecimal number? (Yes)(no):\n")
    while var_continue.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue = input("Would you like to convert another number? (Yes/No):\n")

var_continue2 = "yes"
while var_continue2 in ["yes","y",""]:
    while True:
        try:
            base36 = input("Input a alphadecimal number:\n").upper()
            base36 = base36.strip().replace(" ", "")
            if base36 == "" or not all(c in alphadecimal_digits for c in base36):
                raise ValueError("Invalid alphadecimal number")
            decimal = 0
            n = len(base36)
            for i in range(n):
                digit = base36[i]
                value = alphadecimal_digits.index(digit)
                power_of_36 = n - 1 - i
                decimal += value * (36 ** power_of_36)
            break
        except ValueError as e:
            print(f"Error: {e}. Please input a valid alphadecimal number.")
    print(decimal)
    var_continue2 = input("Would you like to make another alphadecimal number? (Yes)(no):\n")
    while var_continue2.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue2 = input("Would you like to convert another number? (Yes/No):\n")

