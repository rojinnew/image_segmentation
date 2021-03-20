import os
import numpy as np
from utils import flatten_input, unflatten_input, image_to_mat
import gc

def one_k_means_step(X, k, means):
    """
    one step of K-means 
    X: flattened imag of size m x ch (m is number of pixels, ch is number of features)
    k: int, number of clusters
    means: numpy array of size k x ch 

    returns:
    new_means: np array of size k x ch 
    clusters: np array of size  m x 1
    """
    k, ch = means.shape
    m, ch = X.shape 
    X_padded  = np.repeat(X, repeats = k, axis=0)
    means_padded = np.tile(means,(m,1))
    distance  = np.linalg.norm(X_padded - means_padded, 2, axis = 1)
    distance  = distance.reshape((m,k))
    new_cluster = np.argmin(distance, axis=1)
    cluster_index_padded = np.tile(new_cluster,(k,1))
    cluster_list_padded = np.tile(np.array(list(range(0, k))).reshape((k,1)),(1,m))
    assignmnets =  np.equal(cluster_index_padded, cluster_list_padded).astype(int)
    sum_of_weight = np.sum(assignmnets ,axis = 1).reshape((k,1))
    new_means = np.divide((np.matmul(assignmnets,X)), sum_of_weight) 
    return new_means, new_cluster

def k_cluster(pixel_values, k=3, initial_means=None):
    """
    run K-means clustering
    pixel_values shape: m x n x ch 
    k is number of clusters 
    initial_means shape:  k x ch 

    returns:
    updated_pixel_values numpy.array of size m x n x ch
    """
    h, w, ch  = pixel_values.shape
    m = h*w
    old_cluster = np.array([-1]*(m))
    x = flatten_input(pixel_values)
    if initial_means is None:
        initial_means = x[np.random.choice(x.shape[0], k),:]
    max_iter, iter = 10, 0

    while True:
        new_means, new_cluster = one_k_means_step(x, k, initial_means)
        if np.array_equal(old_cluster,new_cluster) or iter > max_iter:
            break
        old_cluster = np.copy(new_cluster)
        initial_means = np.copy(new_means)
        del(new_cluster)
        del(new_means)
        gc.collect()
        iter += 1

    new_pixel_values = unflatten_input(new_means[new_cluster], w)
    return new_pixel_values
