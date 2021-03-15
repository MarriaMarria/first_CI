def pal(n):
    n = input("Type a word \n")
    if str(n) == str(n)[::-1]:
        print("It's a palindrome")
        return True
    else:
        print("Nope")
        return False