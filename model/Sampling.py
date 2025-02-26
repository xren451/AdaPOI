import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from scipy.stats import rv_discrete
from collections import defaultdict


def knn_sampling(poi_data, n_samples=50, k=5):
    """
    KNN-based sampling: Selects POIs by finding representative points using nearest neighbors.
    """
    nbrs = NearestNeighbors(n_neighbors=k).fit(poi_data)
    distances, indices = nbrs.kneighbors(poi_data)
    sampled_indices = np.random.choice(len(poi_data), size=n_samples, replace=False)
    sampled_pois = poi_data.iloc[sampled_indices]
    return sampled_pois


def density_based_sampling(poi_data, eps=0.1, min_samples=5):
    """
    Density-based sampling: Uses DBSCAN to identify dense regions and samples from those clusters.
    """
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(poi_data)
    poi_data["cluster"] = clustering.labels_
    sampled_pois = poi_data.groupby("cluster").apply(lambda x: x.sample(1) if len(x) > 0 else x).reset_index(drop=True)
    return sampled_pois


def importance_sampling(poi_data, importance_column, n_samples=50):
    """
    Importance sampling: Selects POIs based on a weighted probability distribution.
    """
    weights = poi_data[importance_column] / poi_data[importance_column].sum()
    sampled_indices = np.random.choice(len(poi_data), size=n_samples, replace=True, p=weights)
    sampled_pois = poi_data.iloc[sampled_indices]
    return sampled_pois


def category_aware_sampling(poi_data, category_column, n_samples=50):
    """
    Category-aware sampling: Ensures diversity by selecting POIs evenly across categories.
    """
    category_groups = poi_data.groupby(category_column)
    category_samples = defaultdict(list)

    for category, group in category_groups:
        num_samples = max(1, int(n_samples * (len(group) / len(poi_data))))  # Proportional allocation
        category_samples[category] = group.sample(n=min(num_samples, len(group)))

    sampled_pois = pd.concat(category_samples.values()).reset_index(drop=True)
    return sampled_pois