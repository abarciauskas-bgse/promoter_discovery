import numpy as np

def longest_common_substring_length(seq1, seq2):
    seq1_len, seq2_len = [len(seq1), len(seq2)]
    mat = np.zeros((seq1_len, seq2_len))
    z = 0
    substrings = set()
    for i in range(1, seq1_len):
        for j in range(1, seq2_len):
            if seq1[i] == seq2[j]:
                if i == 1 or j == 1:
                    mat.itemset((i,j), 1)
                else:
                    prev_score = mat.item(i-1, j-1)
                    mat.itemset((i,j), prev_score+1)
                if mat.item(i,j) > z:
                    z = mat.item(i,j)
                    #substrings = set(list(seq1)[int(i-z+1):i])
                # elif mat.item(i,j) == z:
                #     #substrings.add(list(seq1)[int(i-z+1):i])
            else:
                mat.itemset((i,j), 0)
    return z
