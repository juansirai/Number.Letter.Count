from NumberToText import number_to_text, count_char_number

total = 0

for number in range(1, 1001):
    long = count_char_number(number_to_text(number))
    total = total + long
    # uncomment to check number by number
    # print(number_to_text(number) + ': ' + str(long))

print(f'total: {total}')
