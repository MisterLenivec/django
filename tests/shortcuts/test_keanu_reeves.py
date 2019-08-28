from django.shortcuts import keanu_reeves
from django.test import SimpleTestCase


class KeanuReevesTests(SimpleTestCase):
    def test_keanu_reeves(self):
        self.assertEqual(keanu_reeves(), 'You are breathtaking!')

