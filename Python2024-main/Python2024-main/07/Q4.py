# Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.

def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    frequency_dict = char_frequency(input_string)
    print("Character frequency:", frequency_dict)
