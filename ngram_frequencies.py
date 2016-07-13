def ngram_frequencies(sequence, n):
    """
    Returns dictionary of frequencies
    """
    frequencies = {}
    for i in range(len(sequence)-n+1):
        ngram = ''.join(sequence[i:(i+n)])
        if ngram in frequencies:
            frequencies[ngram] = frequencies[ngram] + 1
        else:
            frequencies[ngram] = 1
    return frequencies
