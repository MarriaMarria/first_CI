def pal():
    n = input("Type a word \n")
    if str(n) == str(n)[::-1]:
        print("It's a palindrome")
    else:
        print("Nope")