from networkx.classes import is_empty

from src.error import PigLatinError


class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self.phrase == "":
            return "nil"

        first_letter = self.phrase[0]
        if first_letter in "aeiou":
            last_letter = self.phrase[len(self.phrase) - 1]
            if last_letter in "aeiou":
                return self.phrase + "yay"
            if last_letter == "y":
                return self.phrase + "nay"
            return self.phrase + "ay"

        found = False
        i = 0
        while not found and i < len(self.phrase):
            letter = self.phrase[i]
            if letter in "aeiou":
                found = True
            else:
                i += 1
        first_part = self.phrase[0:i]
        second_part = self.phrase[i:]
        return second_part + first_part + "ay"