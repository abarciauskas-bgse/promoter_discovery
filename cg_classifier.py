execfile('ngram_frequencies.py')
errors = 0
num_trials = 100000
for i in range(num_trials):
    freqs = ngram_frequencies(X[i], 2)
    if 'CG' in freqs:
        cg_frequency = freqs['CG']
        true_class = y[i]
        predicted_class = 0
        if cg_frequency <= 32: predicted_class = 1
        if true_class != predicted_class:
            #print 'True class - Predicted class: {0} - {1}'.format(true_class, predicted_class)            
            errors += 1

1 - float(errors)/num_trials
