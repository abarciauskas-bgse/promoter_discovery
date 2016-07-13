import numpy as np

def partition(X, y, index_sets):
    # TODO: Assert X and y are numpy arrays
    # TODO: randomized index sets option
    X_partitioned = np.empty((len(index_sets), X.shape[0]/len(index_sets), X.shape[1]), dtype = str)
    y_partitioned = []
    for i,s in enumerate(index_sets):
        X_partitioned[i,:] = X[s,:]
        y_partitioned.append(y[s])
    return [np.array(X_partitioned), np.array(y_partitioned)]
