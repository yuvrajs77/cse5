def main():
    # python program to find greatest of three numbers
    flag = 1
    number1 = int(input("Enter the first number here :"))
    number2 = int(input("Enter the second number here :"))
    number3 = int(input("Enter the third number here :"))

    if (number1 > number2):
       if(number1 > number3):
            print("Number 1 is greatest")
            flag = 2

    elif (number2 > number1):
        if(number2 > number3):
            print("Number 2 is greatest")
            flag = 3

    if (flag == 1):
        print("Number 3 is greatest")

main()

