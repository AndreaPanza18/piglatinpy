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

    def test_translate_word_starting_vowel_ending_vowel(self):
        translator = PigLatinTranslator("apple")
        phrase = translator.translate()
        self.assertEqual("appleyay", phrase)

    def test_translate_word_starting_vowel_ending_consonant(self):
        translator = PigLatinTranslator("ask")
        phrase = translator.translate()
        self.assertEqual("askay", phrase)

    def test_translate_word_starting_consonant_h(self):
        translator = PigLatinTranslator("hello")
        phrase = translator.translate()
        self.assertEqual("ellohay", phrase)

    def test_translate_word_starting_consonant_w(self):
        translator = PigLatinTranslator("word")
        phrase = translator.translate()
        self.assertEqual("ordway", phrase)

    def test_translate_word_starting_with_two_consonant(self):
        translator = PigLatinTranslator("known")
        phrase = translator.translate()
        self.assertEqual("ownknay", phrase)

    def test_translate_only_consonant(self):
        translator = PigLatinTranslator("fly")
        phrase = translator.translate()
        self.assertEqual("flyay", phrase)