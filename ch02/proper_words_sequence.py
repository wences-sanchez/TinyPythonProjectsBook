"""
This module checks if the second word of a pair ('a', noun) starts with a vowel or not.
If it does, then adds <'n'> to 'a'
"""


class ProperWordsSequence:
    def __init__(self, article, noun):
        self.article = article
        self.noun = noun

    def __repr__(self):
        return self.article + ' ' + self.noun

    def adapt_article_to_noun(self):
        """
        If the noun starts with a vowel and also the article,
        it appends a 'n' to the end of the article
        """
        if self._is_vowel(self.article[-1]) and self._is_vowel(self.noun[0]):
            self.article += 'n'

    @staticmethod
    def _is_vowel(char):
        return char in ['a', 'e', 'i', 'o', 'u']
