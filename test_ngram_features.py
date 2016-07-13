import unittest
execfile('ngram_features.py')

class NgramFrequenciesTest(unittest.TestCase):
    def test_ngram_frequences(self):
        sequence = ['G', 'G', 'T', 'C', 'C', 'A', 'G', 'G']
        frequencies = {'GG': 2, 'GT': 1, 'TC': 1, 'CC': 1, 'CA': 1, 'AG': 1}
        bigram_dict = {key: i for i, key in enumerate(frequencies.keys())}
        self.assertEqual(ngram_features(sequence, 2, bigram_dict), [1, 1, 1, 1, 2, 1])
