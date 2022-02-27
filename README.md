# Number Letter Count

![alt](https://d1rytvr7gmk1sx.cloudfront.net/wp-content/uploads/2020/01/python-developer.jpg)

Number Letter Count, is a Python script which counts the total chars, in numbers between 1 - 1000 (excluding blank spaces & "-".

## 🎯 Problem approach
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage

## 🎯 Installation

Import number_to_text, count_char_number from NumberToText.py

```bash
from NumberToText import number_to_text, count_char_number
```

## 🎯 Usage

```python
from NumberToText import number_to_text, count_char_number

# stores the total number of chars
total = 0

for number in range(1, 1001):
    long = count_char_number(number_to_text(number))
    total = total + long
    # uncomment to check number by number
    # print(number_to_text(number) + ': ' + str(long))

print(f'total: {total}')
```

## 🎯 Main functions explained

### 📌 number_to_text
```python
def number_to_text(number: int) -> str:
    """
    :param number: between 1 and 1000
    :return: number in words
    """
```
This function accepts an integer between 1 and 1000 as param, and returns the same number written in words.
To perform that, it uses:
* a dictionary with "main" number conversions (From 1 to 20 and then the tens and hundreds).
 ```python
   number_dict = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven',  12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty',  90: 'ninety', 100: 'one hundred', 200: 'two hundred', 300: 'three hundred',
        400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred',
        900: 'nine hundred', 1000: 'one thousand'
  ```
* auxiliar function "compound_number" which pursuits the same objetive for numbers which doesn't belong to the dictionary.

### 📌 compound_number
```python
def compound_number(n: int) -> str:
  """
  :param n: compound number less than 100
  :return: compound number in words
  """
```
For a compound number, we need to decompose it in the main number plus the residue.
For eg, if we work with 32: residue = 2 and main_number = 30 (for numbers below 100)
After that, we can convert it in words by searching into the base dictionary for the main number, and for the residue in separate ways:
```python
result = number_dict[main_number] + "-" + number_dict[residue]
```

### 📌 count_char_number
```python
def count_char_number(string: str) -> int:
    """
    :param string: number written as a text
    :return: number of char in the number, without blanks and "-".
    """
```
Used to count total chars in a word, excluding blank spaces and "-".


