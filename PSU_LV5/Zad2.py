import scipy as sp
from sklearn import cluster, datasets
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X


data = generate_data(500, 1)
kmeans = cluster.KMeans(n_clusters = 5, random_state = 0, n_init = "auto").fit(data)
kmeans_centers = kmeans.cluster_centers_
kmeans_predict = kmeans.predict(data)
plt.scatter(data[:,0], data[:,1], c = kmeans_predict)
plt.scatter(kmeans_centers[:,0], kmeans_centers[:,1], marker = 'x', s = 100, color = 'black')
plt.show()

