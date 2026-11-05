from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        translator = PigLatinTranslator("hello world")
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_traslate_empty_string(self):
        translator = PigLatinTranslator("")
        phrase = translator.translate()
        self.assertEqual("nil", phrase)

    def test_translate_word_starting_vowel_a_ending_y(self):
        translator = PigLatinTranslator("any")
        phrase = translator.translate()
        self.assertEqual("anynay", phrase)

    def test_translate_word_starting_vowel_e_ending_y(self):
        translator = PigLatinTranslator("enemy")
        phrase = translator.translate()
        self.assertEqual("enemynay", phrase)