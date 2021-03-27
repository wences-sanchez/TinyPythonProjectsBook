import unittest

from ch02.proper_words_sequence import ProperWordsSequence


class ProperWordsSequenceTest(unittest.TestCase):
    """
    Tests if the first of two words doesn't end with a vowel
    when the second word starts with one vowel
    """

    def test_article_ends_consonant_when_noun_starts_with_vowel(self):
        proper_words_sequence = ProperWordsSequence(article='a', noun='ice')
        proper_words_sequence.adapt_article_to_noun()
        self.assertNotIn(proper_words_sequence.article[-1], ['a', 'e', 'i', 'o', 'u'])

        proper_words_sequence = ProperWordsSequence(article='a', noun='element')
        proper_words_sequence.adapt_article_to_noun()
        self.assertNotIn(proper_words_sequence.article[-1], ['a', 'e', 'i', 'o', 'u'])

        proper_words_sequence = ProperWordsSequence(article='a', noun='aid')
        proper_words_sequence.adapt_article_to_noun()
        self.assertNotIn(proper_words_sequence.article[-1], ['a', 'e', 'i', 'o', 'u'])

    def test_article_doesnt_change_when_noun_starts_with_consonant(self):
        proper_word_sequence = ProperWordsSequence(article='a', noun='smile')
        proper_word_sequence.adapt_article_to_noun()
        article_after = proper_word_sequence.article
        self.assertEqual(article_after, 'a')

    def test_article_doesnt_change_when_noun_starts_with_consonant_but_article_ends_in_n(self):
        proper_word_sequence = ProperWordsSequence(article='an', noun='alphabet')
        proper_word_sequence.adapt_article_to_noun()
        article_after = proper_word_sequence.article
        self.assertEqual(article_after, 'an')


if __name__ == '__main__':
    unittest.main()
