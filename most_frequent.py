def most_frequent(s):
    char_frequency = {}
 
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1

        else:
            char_frequency[char] = 1
    sorted_char_frequency = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)
 
    for char, frequency in sorted_char_frequency:
        print(char, end='')
input_string = input("Enter a string: ")
most_frequent(input_string)