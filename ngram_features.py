import ngram_frequencies as nf

def ngram_features(sequence, n, ngram_dict):
    ngram_freqs = nf.ngram_frequencies(sequence, n)
    ngram_freqs_features = [0]*len(ngram_dict)
    for key, idx in ngram_dict.iteritems():
        if key in ngram_freqs:
            ngram_freqs_features[idx] = ngram_freqs[key]
        else:
            ngram_freqs_features[idx] = 0
    return ngram_freqs_features    
