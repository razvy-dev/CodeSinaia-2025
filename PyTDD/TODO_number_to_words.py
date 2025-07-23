digits = {
    0: "zero",
    1: "one",  
    2: "two",
    3: "three",
    4: "four",
    5: "five", 
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

reversed_digits = {v: k for k, v in digits.items()}

teen = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

ty = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

zecimals = {
    2: "hundred",
    3: "thousand",
    4: "million",
}

def number_to_words(n):
    type = isinstance(n, int)
    word = "zero"
    count = 0
    if n == None:
        return None
    elif not type:
        raise TypeError("Input must be a string")
    else:
        while n > 0:
            digit = n % 10
            n //= 10
            count += 1
            if count == 1:
                word = digits[digit]
            elif count == 2:
                if word == "zero":
                    print(digit*10)
                    word = ty[digit*10]
                elif digit == 1:
                    word = teen[10+reversed_digits[word]]
                else:
                    word = ty[digit*10] + " " + word
            elif count == 3:
                if word is in ty.items():
                    word = digits[digit] + " " + zecimals[count]

        return word