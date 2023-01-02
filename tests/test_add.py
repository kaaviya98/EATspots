from django.test import TestCase


class TestAddition(TestCase):
    def test_1_plus_1(self):
        self.assertEqual(2, 1 + 1)
