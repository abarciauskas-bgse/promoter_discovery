import ngram_frequencies as nf

def ngram_features(sequence, n, ngram_dict):
    """
    Maps an array of strings to a 1-d array of the length of the number of keys in ngram_dict.
    Used to create a vector of ngram features used in classification.
    
    Parameters
    ----------
    sequence : array of strings
    n : length of n gram
    ngram_dict: dictionary mapping ngram keys to index in feature array

    Returns
    -------
    array of values representing a frequency of an ngram in the sequence.
    """      
    ngram_freqs = nf.ngram_frequencies(sequence, n)
    ngram_freqs_features = [0]*len(ngram_dict)
    for key, idx in ngram_dict.iteritems():
        if key in ngram_freqs:
            ngram_freqs_features[idx] = ngram_freqs[key]
        else:
            ngram_freqs_features[idx] = 0
    return ngram_freqs_features    
