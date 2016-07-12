import os, sys
from pysam import FastaFile
import glob
import numpy as np

"""
Helper code for extracting DNA sequence with 
corresponding labels from genome.

"""

def iter_peaks_and_labels(fname):
    """
    Parse '.bed' file into a key value pair tuple.
    
    Parameters
    ----------
    fname : '.bed' file with label & location information

    Returns
    -------
    Generator of parsed file 
    format: (('chr1', start_idx, end_idx), label)
    """

    with open(fname) as fp:
        for line in fp:
            data = line.split()
            if data:
                yield (data[0], int(data[1]), int(data[2])), data[3]
    return


def data_iter(genome_path, label_file):
    """
    Extract 1000 long base pair sequences with corresponding labels.

    Parameters
    ----------
    genome_path :  '.genome.fa' file with genome sequence
    label_file  :  '.bed' file with label & location information

    Returns
    -------
    Generator of extracted 1000 long base pair sequence
    format: ((region, label), sequence))
    """

    min_region_size = 1000
    
    genome = FastaFile(genome_path)
    
    for region, label in iter_peaks_and_labels(label_file):
        # create a new region exactly min_region_size basepairs long centered on 
        # region  
        expanded_start = region[1] + (region[2] - region[1])/2 - min_region_size/2
        expanded_stop = expanded_start + min_region_size
        region = (region[0], expanded_start, expanded_stop)
        yield ((region, label), genome.fetch(*region))
    return


def base_encoding(files, genome_file):
    """
    Generate input data matrix and label vector.

    Parameters
    ----------
    files       :  list of '.bed' file names
    genome_file :  '.genome.fa' file with genome sequence

    Returns
    -------
    X : numpy array of extracted base pair ('A', 'T', 'C', 'G', 'N' = unknown) 
        shape = (num_observations, 1000)
    y : numpy array of binary labels (promoter = 0, enhancer = 1)
        shape = (num_observations,)
    """
    
    data = []
    target = []

    for label_file in files:
        iterator = data_iter(genome_file, label_file)

        for x in iterator:
            data.append(list(x[1]))

            if x[0][1] == 'promoter':
                target.append(0)
            else:
                target.append(1)

    X = np.array(data).astype(str)
    y = np.array(target).astype(int)

    print("Generated X with shape ", X.shape)
    print("Generated y with shape ", y.shape)
    
    return (X, y)

if __name__ == '__main__':
    
    bed_files = glob.glob("RAMPAGE_peaks/train_data/*.bed")
    genome_file = "RAMPAGE_peaks/train_data/GRCh38.genome.fa"

    X, y = base_encoding(bed_files, genome_file)
