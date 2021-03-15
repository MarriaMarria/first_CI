def average():
    sentence = input("Please type your sentence:\n")
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)