import unittest
execfile('partition.py')

class ParititionTest(unittest.TestCase):
    def test_partition(self):
        X = [['G', 'G', 'T', 'G', 'G', 'C'],
             ['T', 'C', 'C', 'C', 'C', 'T'],
             ['C', 'T', 'C', 'A', 'C', 'C'],
             ['T', 'C', 'T', 'A', 'G', 'C'],
             ['G', 'C', 'C', 'A', 'C', 'T'],
             ['T', 'T', 'G', 'C', 'C', 'G']]
        y = [0, 1, 1, 1, 0, 1]
        index_sets = [[3,4],[0,2],[1,5]]
        n_partitions = 3
        X_partitioned, y_partitioned = partition(X, y, n_partitions, index_sets)
        self.assertEqual(len(X_partitioned), n_partitions)
        self.assertEqual(len(y_partitioned), n_partitions)
        self.assertEqual(X_partitioned[0][0], ['T', 'C', 'T', 'A', 'G', 'C'])
        self.assertEqual(y_partitioned[0][0], 1)
