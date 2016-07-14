def ngram_frequencies(sequence, n):
    """
    Maps an array of strings to a dictionary of frequencies for each ngram represented in the sequence.
    
    Parameters
    ----------
    sequence : array of strings
    n : length of n gram

    Returns
    -------
    Dictionary of frequencies
    """
    frequencies = {}
    for i in range(len(sequence)-n+1):
        ngram = ''.join(sequence[i:(i+n)])
        if ngram in frequencies:
            frequencies[ngram] = frequencies[ngram] + 1
        else:
            frequencies[ngram] = 1
    return frequencies
