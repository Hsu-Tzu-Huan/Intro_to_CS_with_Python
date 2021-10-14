A = 0
B = 0
num1 = input("Please enter the first Number:" )
if len(num1) != 4:
    print("Please enter a four digit number.")

elif (num1[0] != num1[1] and \
    num1[0] != num1[2] and \
    num1[0] != num1[3] and \
    num1[1] != num1[2] and \
    num1[1] != num1[3] and \
    num1[2] != num1[3]):
    num2 = input("Please enter the second number:" )

    if len(num2) != 4:
        print("Please enter a four digit number.")

    elif (num2[0] != num2[1] and \
        num2[0] != num2[2] and \
        num2[0] != num2[3] and \
        num2[1] != num2[2] and \
        num2[1] != num2[3] and \
        num2[2] != num2[3]):

        if num2[0] == num1[0]:
            A += 1
        elif num2[0] in num1:
            B += 1
        if num2[1] == num1[1]:
            A += 1
        elif num2[1] in num1:
            B += 1
        if num2[2] == num1[2]:
            A += 1
        elif num2[2] in num1:
            B += 1
        if num2[3] == num1[3]:
            A += 1
        elif num2[3] in num1:
            B += 1

        if A == 4:
            print("Well Done!")

        print(f"The first number:{num1}")
        print(f"The second number:{num2}")
        print(f"The result of comparison:{A}A{B}B")
        print("Let's try again :P")

    else:
        print("Please enter the numbers again. The digits can't be repeated.")
        
else:
    print("Please enter the numbers again. The digits can't be repeated.")