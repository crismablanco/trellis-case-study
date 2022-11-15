class NumbersService:
    """
    Class to convert numbers into english words
    """

    units = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thriteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "fourty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    # Hundreds definition.
    # If need more espressions, just add them here
    # DESCENDENT ORDER
    hundreds = {
        1e45: "quattuordecillion",
        1e42: "tredecillion",
        1e39: "duodecillion",
        1e36: "undecillion",
        1e33: "decillion",
        1e30: "nonillion",
        1e27: "octillion",
        1e24: "septillion",
        1e21: "hextillion",
        1e18: "quintillion",
        1e15: "quadrillion",
        1e12: "trillion",
        1e9: "billion",
        1e6: "million",
        1e3: "thousand",
        1e2: "hundred",
    }

    ALERT_BIG_NUMBER = "The given number is too big"

    def __init__(self, and_word: str = "and") -> None:
        # initialize the object with empty "and_word" if don't want the expression
        self.and_word = and_word

    def convert(self, number: int) -> str:
        expression = self.__convert_to_english(number=number)
        return self.clean_stop_words(expression=expression)

    def clean_stop_words(self, expression: str) -> str:
        if expression.startswith(self.and_word):
            return expression[len(self.and_word) :].strip()
        return expression.strip()

    def __number_less_than_100(self, number: int) -> str:
        quotient, remainder = divmod(number, 10)
        second_expression = ""
        if self.and_word:
            first_expression = f"{self.and_word} {self.tens[int(quotient)]}"
        else:
            first_expression = self.tens[int(quotient)]

        if remainder:
            second_expression = f" {self.__convert_to_english(remainder)}"

        return f"{first_expression}{second_expression}"

    def __build_hundreds(
        self, quotient: int, remainder: str, hundred_expression: str
    ) -> str:
        first_expression = self.__convert_to_english(quotient)
        second_expression = ""
        if remainder:
            second_expression = f" {self.__convert_to_english(remainder)}"
        return f"{first_expression} {hundred_expression}{second_expression}"

    def __convert_to_english(self, number: int) -> str:
        if isinstance(number, int) and number >= 0:
            # validation
            if number > list(self.hundreds.keys())[0]:
                return self.ALERT_BIG_NUMBER

            # units
            if number < 20:
                return self.units[number]

            # tens
            if number < 100:
                return self.__number_less_than_100(number=number)

            # hundreds
            for key, value in self.hundreds.items():
                quotient, remainder = divmod(number, key)
                if quotient:
                    return self.__build_hundreds(
                        hundred_expression=value,
                        quotient=int(quotient),
                        remainder=int(remainder),
                    )

        return ""
