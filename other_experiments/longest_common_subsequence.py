import numpy as np

def longest_common_subsequence_score(seq1, seq2):
    seq1_len, seq2_len = [len(seq1), len(seq2)]
    score_matrix = np.zeros((seq1_len, seq2_len))
    for i in range(1,seq1_len):
        for j in range(1,seq2_len):
            if seq1[i] == seq2[j]:
                score_matrix.itemset((i,j), score_matrix.item(i-1,j-1) + 1)
            else:
                val1 = score_matrix.item((i-1,j))
                val2 = score_matrix.item((i,j-1))
                better_score = max(val1, val2)
                score_matrix.itemset((i,j), better_score)
    return score_matrix[seq1_len-1, seq2_len-1]

