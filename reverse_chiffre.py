def reverse_chiffre():
    my_number =str(input("Please type in a number bigger than 9: \n"))
    check = my_number[0] 
    if check == "-": 
        number = my_number[1:]
        print(number)
    else:
        number = "-" + my_number
        print(number)


reverse_chiffre()