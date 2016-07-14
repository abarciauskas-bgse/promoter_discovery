import numpy as np

def partition(X, y, index_sets):
    """
    Partition data into number of sets in index_sets, used for k-fold cross valiation
    
    Parameters
    ----------
    X : feature data, numpy ndarray, first dimension should be number of total observations
    y : label data, 1-d numpy array
    index_sets: array of arrays, k arrays each of length number of observations / k

    Returns
    -------
    [X_partitioned, y_partitioned]
    """    
    # TODO: Assert X and y are numpy arrays
    X_partitioned = np.empty((len(index_sets), X.shape[0]/len(index_sets), X.shape[1]), dtype = str)
    y_partitioned = []
    for i,s in enumerate(index_sets):
        X_partitioned[i,:] = X[s,:]
        y_partitioned.append(y[s])
    return [np.array(X_partitioned), np.array(y_partitioned)]
