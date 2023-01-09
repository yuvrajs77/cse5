def main():
    input = "Python is a case sensitive language"

    #a) Find the length of the input string
    print(len(input))

    #b) Reverse the order of the string in one line code
    print(input[::-1])

    #c) Using the slice function store " a case sensitive language" in new string 
    new_string = slice(9,27)
    print(input[new_string])

    #d) Replace a "case sensitive" with "object orientied"
    replaced_string = input.replace("case sensitive" , "object oriented")
    print(f"{replaced_string}")
    
    #e) Remove the white spaces from the given input string 
    input1 = "   Python is a case sensitive language".strip()
    print(f"{input1}")

main()
