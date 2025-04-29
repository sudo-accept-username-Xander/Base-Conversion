var_continue = "yes"
while var_continue in ["yes","y",""]:
    while True:
        try:
            base10 = input("Input a base 10 number:\n").strip()
            devider = int(base10)
            if devider < 0:
                raise ValueError
            if devider == 0:
                binary = "0"
            else:
                binary = ""
                while devider > 0:
                    remainder = devider % 2
                    devider = devider // 2
                    binary = str(remainder) + binary
            break
        except ValueError:
            print("Please input a valid non-negative base 10 number.")
    print(binary)
    var_continue = input("Would you like to convert another number? (Yes/No):\n").strip()
    while var_continue.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue = input("Would you like to convert another number? (Yes/No):\n").strip()

var_continue2 = "yes"
while var_continue2 in ["yes","y",""]:
    while True:
        try:
            base2 = input("Input a binary number:\n").strip()
            if base2 == "" or not all(c in "01" for c in base2):
                raise ValueError("Invalid binary number")
            decimal = 0
            n = len(base2)
            for i in range(n):
                bit = int(base2[i])
                power_of_2 = n - 1 - i
                decimal = decimal + bit * (2 ** power_of_2)
            break
        except ValueError as e:
            print(f"Error: {e}. Please input a valid binary number.")
    print(decimal)
    var_continue2 = input("Would you like to convert another number? (Yes/No):\n").strip()
    while var_continue2.lower() not in ["yes","y","","no","n"]:
        print("Please put either a yes or a no.")        
        var_continue2 = input("Would you like to convert another number? (Yes/No):\n").strip()

