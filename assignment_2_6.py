def main():
    # program to check whether the given input of 3 numbers can form a triangle or no
    flag = 2 # to verify if statements are executed or not
    side1 = int(input('Enter the 1st side here : '))
    side2 = int(input('Enter the 2nd side here : '))
    side3 = int(input('Enter the 3rd side here : '))

    if(side1 + side2 < side3):
        print("no")
        flag = 1
        
    if(side2 + side3 < side1):
        print("no")
        flag = 1 
    
    if(side1 + side3 < side2):
        print("no")
        flag = 1
    
    if(flag == 2):
        print("yes")

main()