import numpy as np

def needlman_wunsch(seq1, seq2):
    """
    Global sequence alignment
    
    Parameters
    ----------
    seq1 : array of strings
    seq2 : array of strings

    Returns
    -------
    Needleman-Wunsch score for best global alignment
    """     
    gap_penalty = -1
    dissim_penalty = -1
    sim_penalty = +1
    seq1_len, seq2_len = [len(seq1), len(seq2)]
    score_matrix = np.zeros((seq1_len+1, seq2_len+1))
    score_matrix[0,:] = [i*gap_penalty for i in range(seq1_len+1)]
    score_matrix[:,0] = [i*gap_penalty for i in range(seq2_len+1)]
    for i in range(1,seq1_len):
        for j in range(1,seq2_len):
            simij = sim_penalty if seq1[i-1] == seq2[j-1] else dissim_penalty
            # score so far if aligned at i-1, j-1
            qdiag = score_matrix.item((i-1,j-1)) + simij
            # score so far if adding gap to seq1 (I think seq1, need to check this)
            qup = score_matrix.item((i-1,j)) + gap_penalty
            # score so far if adding gap to seq2
            qdown = score_matrix.item((i,j-1)) + gap_penalty
            score_matrix.itemset((i,j), max(qdiag, qup, qdown))
    final_score = score_matrix[seq1_len-1,seq2_len-1]
    return final_score
