# Roman <-> Decimal Smart Converter
# Advanced Python Mini Project

ROMAN_MAP = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100,
    'D': 500, 'M': 1000
}

ROMAN_VALUES = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def decimal_to_roman(num):
    if not (1 <= num <= 3999):
        return "Error: Enter number between 1-3999"

    result = ""

    for value, symbol in ROMAN_VALUES:
        while num >= value:
            result += symbol
            num -= value

    return result


def roman_to_decimal(roman):
    roman = roman.upper()

    if not all(char in ROMAN_MAP for char in roman):
        return "Error: Invalid Roman numeral"

    total = 0
    prev = 0

    for char in reversed(roman):
        value = ROMAN_MAP[char]

        if value < prev:
            total -= value
        else:
            total += value

        prev = value

    return total


def display_banner():
    print("=" * 50)
    print("      ROMAN ↔ DECIMAL SMART CONVERTER")
    print("=" * 50)


def main():
    while True:
        display_banner()

        print("\nSelect Conversion Type:")
        print("1. Decimal → Roman")
        print("2. Roman → Decimal")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == '1':
            try:
                num = int(input("Enter Decimal Number: "))
                print(f"Roman Numeral: {decimal_to_roman(num)}")
            except ValueError:
                print("Invalid input! Enter integer.")

        elif choice == '2':
            roman = input("Enter Roman Numeral: ")
            print(f"Decimal Number: {roman_to_decimal(roman)}")

        elif choice == '3':
            print("Thanks for using converter!")
            break

        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")


main()