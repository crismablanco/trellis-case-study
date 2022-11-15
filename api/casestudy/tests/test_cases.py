from django.test import TestCase
from casestudy.services import NumbersService


class TestService(TestCase):  # pragma: no cover
    def test_convert(self):
        expected_words = {
            0: "zero",
            1: "one",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            20: "twenty",
            40: "fourty",
            66: "sixty six",
            99: "ninety nine",
            100: "one hundred",
            298888: "two hundred and ninety eight thousand eight hundred and eighty eight",
            1e50: "The given number is too big",
            -1: "",
        }
        and_word = "and"
        numbers_service = NumbersService(and_word=and_word)
        self.assertEqual(numbers_service.and_word, "and")

        for number, word in expected_words.items():
            number_in_english = numbers_service.convert(number=int(number))
            self.assertEqual(number_in_english, word)

        and_word = ""
        numbers_service = NumbersService(and_word=and_word)
        self.assertEqual(numbers_service.and_word, "")
        number_in_english = numbers_service.convert(number=40)
        self.assertEqual(number_in_english, "fourty")
