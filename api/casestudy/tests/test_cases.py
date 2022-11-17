from django.test import TestCase
from rest_framework.test import APIClient

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
            -1: "",  # only positive integers
        }
        and_word = "and"
        numbers_service = NumbersService(and_word=and_word)
        self.assertEqual(numbers_service.and_word, "and")

        for number, word in expected_words.items():
            number_in_english = numbers_service.convert(number=int(number))
            self.assertEqual(number_in_english, word)

        # test without and_word
        and_word = ""
        numbers_service = NumbersService(and_word=and_word)
        self.assertEqual(numbers_service.and_word, "")
        number_in_english = numbers_service.convert(number=40)
        self.assertEqual(number_in_english, "fourty")

        # test not numbers
        number_in_english = numbers_service.convert(number="I'm not a number")
        self.assertEqual(number_in_english, "")

        # test float
        number_in_english = numbers_service.convert(number=20.4)
        self.assertEqual(number_in_english, "")


class EndpointTests(TestCase):
    def test_endpoints(self):
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
        }

        client = APIClient()
        for number, word in expected_words.items():
            request = client.get(f"/num_to_english/?number={int(number)}&and_word=and")
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request.data["num_in_english"], word)
            self.assertEqual(request.data["status"], "ok")

            request = client.post(
                "/num_to_english/", dict(number=int(number), and_word="and")
            )
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request.data["num_in_english"], word)
            self.assertEqual(request.data["status"], "ok")

        # bad requests
        # without query param
        request = client.get("/num_to_english/")
        self.assertEqual(request.status_code, 500)
        self.assertEqual(request.data["num_in_english"], "")
        self.assertEqual(request.data["status"], "fail")

        # without body param
        request = client.post("/num_to_english/")
        self.assertEqual(request.status_code, 500)
        self.assertEqual(request.data["num_in_english"], "")
        self.assertEqual(request.data["status"], "fail")

        # float param
        request = client.get("/num_to_english/?number=0.9")
        self.assertEqual(request.status_code, 500)
        self.assertEqual(request.data["status"], "fail")

        # not a number param
        request = client.get("/num_to_english/?number=not-a-number")
        self.assertEqual(request.status_code, 500)
        self.assertEqual(request.data["status"], "fail")

        request = client.get("/num_to_english/?number=1e20")
        self.assertEqual(request.status_code, 500)
        self.assertEqual(request.data["status"], "fail")
