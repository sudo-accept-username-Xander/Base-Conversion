var_continue = "yes"
while var_continue in ["yes","y",""]:
    while True:
        try:
            base10 = input("Input a base 10 number:\n").strip()
            divider = int(base10)
            if divider < 0:
                raise ValueError
            if divider == 0:
                octal = "0"
            else:
                octal = ""
                while divider > 0:
                    remainder = divider % 8
                    octal = str(remainder) + octal
                    divider = divider // 8
            break
        except ValueError:
            print("Please input a valid non-negative base 10 number.")
    print(octal)
    var_continue = input("Would you like to convert another number? (Yes/No):\n").strip()
    while var_continue.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue = input("Would you like to convert another number? (Yes/No):\n").strip()

var_continue2 = "yes"
while var_continue2 in ["yes","y",""]:
    while True:
        try:
            base8 = input("Input a octal number:\n").upper().strip()
            if base8 == "" or not all(c in "01234567" for c in base8):
                raise ValueError("Invalid octal number")
            decimal = 0
            n = len(base8)
            for i in range(n):
                digit = int(base8[i])
                power_of_8 = n - 1 - i
                decimal += digit * (8 ** power_of_8)
            break
        except ValueError as e:
            print(f"Error: {e}. Please input a valid octal number.")
    print(decimal)
    var_continue2 = input("Would you like to convert another number? (Yes/No):\n").strip()
    while var_continue2.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue2 = input("Would you like to convert another number? (Yes/No):\n").strip()

