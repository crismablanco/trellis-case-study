from django.test import TestCase

from casestudy.utils import str2bool


class TestUtils(TestCase):  # pragma: no cover
    def test_str2bool(self):
        expressions = {
            "1": True,
            "y": True,
            "yes": True,
            "true": True,
            "True": True,
            "TRUE": True,
            "-1": False,
            "false": False,
            "False": False,
            "FALSE": False,
            "0": False,
            "f": False,
            "whatever": False,
        }

        for value_to_convert, bool_expression in expressions.items():
            self.assertEqual(str2bool(value=value_to_convert), bool_expression)

        self.assertTrue(str2bool(value=True))
        self.assertFalse(str2bool(value=False))
        self.assertFalse(str2bool(value=""))
