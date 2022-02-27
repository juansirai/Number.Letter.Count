
def number_to_text(number: int) -> str:
    """
    :param number: between 1 and 1000
    :return: number in words
    """

    # dictionary with main number conversions
    number_dict = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven',  12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty',  90: 'ninety', 100: 'one hundred', 200: 'two hundred', 300: 'three hundred',
        400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred',
        900: 'nine hundred', 1000: 'one thousand'
    }

    def compound_number(n: int) -> str:
        """
        :param n: compound number less than 100
        :return: compound number in words
        """
        # for a compound number, we need to decompose it in the main number plus the residue
        # for eg, if we work with 32: residue = 2 and main_number = 30 (for numbers below 100).
        residue = n % 10
        main_number = n - residue
        res = number_dict[main_number] + "-" + number_dict[residue]
        return res

    try:
        # checks if we can convert it directly, by looking into the dictionary
        result = number_dict[number]
    except KeyError:
        if number < 100:
            # if the number is below 100 and doesn't belong to the dictionary, is because it is a
            # compound number.
            result = compound_number(number)
        elif number < 1000:
            # if the number is greater than 100 and lower than 1000, we need to decompose it in the
            # base and residue. In this case, we can work with the residue in a recursive way, calling
            # the same function number_to_text().
            last_digits = number % 100
            main_n = number - last_digits
            result = number_dict[main_n] + ' and ' + number_to_text(last_digits)
        else:
            # if the number is zero or greater than 1000.
            raise Exception('number out of range')
    return result


def count_char_number(string: str) -> int:
    """
    :param string: number written as a text
    :return: number of char in the number, without blanks and "-".
    """
    aux = string.replace(" ", "").replace("-", "")
    return len(aux)
