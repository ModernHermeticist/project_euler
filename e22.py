def main():
    f = open('p022_names.txt', 'r')
    letter_number_value = { 'A': 1,
                            'B': 2,
                            'C': 3,
                            'D': 4,
                            'E': 5,
                            'F': 6,
                            'G': 7,
                            'H': 8,
                            'I': 9,
                            'J': 10,
                            'K': 11,
                            'L': 12,
                            'M': 13,
                            'N': 14,
                            'O': 15,
                            'P': 16,
                            'Q': 17,
                            'R': 18,
                            'S': 19,
                            'T': 20,
                            'U': 21,
                            'V': 22,
                            'W': 23,
                            'X': 24,
                            'Y': 25,
                            'Z': 26
    }
    list_of_lines = []
    a = f.read()
    f.close()
    a = a.replace('"', "")
    word_value = 0
    sum_of_values = 0
    for i in a.split(','):
        list_of_lines.append(i)
    list_of_lines.sort()
    for i, line in enumerate(list_of_lines):
        word_value = 0
        for letter in line:
            word_value += letter_number_value[letter]
        sum_of_values += (word_value * (i+1))

    print(sum_of_values)


main()