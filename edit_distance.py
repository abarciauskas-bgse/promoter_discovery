import numpy as np

def edit_distance(seq1, seq2):
    seq1_len, seq2_len = [len(seq1), len(seq2)]
    score_matrix = np.zeros((seq1_len, seq2_len))    
    score_matrix[0,:] = [i for i in range(seq1_len)]
    score_matrix[:,0] = [i for i in range(seq2_len)]
    for i in range(seq1_len):
        for j in range(seq2_len):
            if seq1[i] == seq2[j]:
                score_matrix.itemset((i,j), score_matrix.item(i-1,j-1))
            else:
                deletion = score_matrix.item((i-1,j)) + 1
                insertion = score_matrix.item((i,j-1)) + 1
                substitution = score_matrix.item((i-1,j-1)) + 1
                score_matrix.itemset((i,j), min(deletion, insertion, substitution))
    return score_matrix.item((seq1_len, seq2_len))
