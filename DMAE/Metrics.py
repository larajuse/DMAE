"""
Implementation of: Dissimilarity Mixture Autoencoder (DMAE) for Deep Clustering.

**This package contains the implementation of the metrics that are used to evaluate DMAE.**

Author: Juan Sebastián Lara Ramírez <julara@unal.edu.co> <https://github.com/larajuse>
"""

import numpy as np
from scipy.optimize import linear_sum_assignment

def unsupervised_classification_accuracy(y_true, y_pred):
    """
    Scipy-based implementation of the unsupervised classification accuracy.
    Arguments:
        y_true: array-like, shape=(n_samples, )
            Array with the Ground truth labels.
        y_pred: array-like, shape=(n_samples)
            Array with the predicted labels.
    Returns:
        uacc: float
            Unsupervised classification accuracy between y_true and y_pred.
    """
    
    D = max(y_pred.max(), y_true.max()) + 1
    w = np.zeros((D, D), dtype=np.int64)
    for i in range(y_pred.size):
        w[y_pred[i], y_true[i]] += 1
    ind = np.array(linear_sum_assignment(w.max() - w)).T
    return sum([w[i, j] for i, j in ind])*1.0/y_pred.size

def L0_norm(preds, thr=1e-7):
    """
    Numpy implementation of the L0 norm.
    Arguments:
        preds: array-like, shape=(n_samples, n_clusters)
            Soft-assignments extracted from a DM-Encoder
        thr: float
            Threshold used to compute the L0 norm.
    Returns:
        L0: float
            L0 norm of the soft-assignments.
    """
    
    counts = (preds>thr).astype("float32").sum(axis=1)
    return counts

class metrics():
    def __init__(self):
        self.unsupervised_classification_accuracy = unsupervised_classification_accuracy
        self.L0_norm = L0_norm