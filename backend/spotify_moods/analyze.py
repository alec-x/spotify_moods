
import math
import numpy as np

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

import umap

def standardize_data(arr: np.array) -> np.array:
    sc = StandardScaler()
    return sc.fit_transform(arr)

def extract_pca(arr: np.array, num_comp: int = 2) -> np.array:
    num_comp = 2
    fit = PCA(n_components=num_comp)
    return fit.fit_transform(arr)

def extract_tsne(arr: np.array, n_comp: int = 2, perp: int = 50, iter: int = 5000, lr: int = 200) -> np.array:
    fit = TSNE(n_components=n_comp, 
        perplexity=perp, 
        n_iter=iter, 
        learning_rate=lr)

    return fit.fit_transform(arr)

def extract_umap(arr: np.array, n_neigh: int = 15, min_dist: int = 0.1, n_comp: int = 2, metric: str = 'euclidean') -> np.array:
    fit = umap.UMAP(n_neighbors=n_neigh, 
        min_dist=min_dist,  
        n_components=n_comp, 
        metric=metric)

    return fit.fit_transform(arr)

def return_similar_songs(embeddings: np.ndarray, song_coords: tuple[int, int], n_songs: int) -> list[str]:
    song_suggestions = []
    distances = []
    a = list(song_coords)

    for i, result in enumerate(embeddings):
        b = list(result)
        
        dist = math.dist(a, b)
        distances.append(dist)
        song_suggestions.append(i)

        if len(distances) > n_songs:
            ind = distances.index(max(distances))
            distances.pop(ind)
            song_suggestions.pop(ind)    

    return song_suggestions