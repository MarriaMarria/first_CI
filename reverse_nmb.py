def reverse_nmb():
    nmb_to_reverse =str(input("Pleasy type in any number (positive or negative) bigger than 0\n"))
    print(type(nmb_to_reverse));

    check = nmb_to_reverse[0]

    if check == "-":
        new_nmb = nmb_to_reverse[1:]
        print(new_nmb)
    else:
        new_nmb = "-" +str(nmb_to_reverse)
        print(new_nmb)

