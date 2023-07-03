def most_frequent(str1):
    count = {}
    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_count:
        print(letter, count)
str1 = input("Please enter a string: ")
most_frequent(str1)
