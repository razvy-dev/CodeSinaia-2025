arab_roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman_numerals = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def roman_converter_to_arab(value):
    if value is None:
        return None
    if isinstance(value, str):
        if not value.isalpha():
            return None
        total = 0
        for c in value:
            if c in arab_roman_dict:
                total += arab_roman_dict[c]
            else:
                return None
        if total < 1 or total >= 4000:
            return None
        return total
    return None

def arab_to_roman_converter(value):
    roman_numerals = ""
    if value is None:
        return None
    if not isinstance(value, int) or value < 1 or value >= 4000:
        return None
    for numeral, arabic in sorted(arab_roman_dict.items(), key=lambda x: x[1], reverse=True):
        while value >= arabic:
            roman_numerals += numeral
            value -= arabic
    return ''.join(roman_numerals)

def main():
    pass

if __name__ == "__main__":
    main()