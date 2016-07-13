import unittest
execfile('ngram_frequencies.py')

class NgramFrequenciesTest(unittest.TestCase):
    def test_ngram_frequences(self):
        sequence = ['G', 'G', 'T', 'C', 'C', 'A', 'G', 'G']
        frequencies = {'GGT': 1, 'GTC': 1, 'TCC': 1, 'CCA': 1, 'CAG': 1, 'AGG': 1}
        self.assertEqual(ngram_frequencies(sequence, 3), frequencies)
