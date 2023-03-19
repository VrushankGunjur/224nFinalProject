import torch
import numpy as np
import csv
import random

eps = 0.00000000000001

def distance_score(embedding, wb_embeddings, clusters, num_clusters):
    #print('correctly using distance score')
    distances = wb_embeddings - embedding
    distances = torch.linalg.norm(distances, dim=1)
    
    cluster_means = [0] * num_clusters
    cluster_counts = [0] * num_clusters
    for cluster, dist in zip(clusters, distances):
        cluster_means[cluster] += dist
        cluster_counts[cluster] += 1
    
    cluster_means = [cluster_means[idx]/cluster_counts[idx] for idx in range(len(cluster_means))]
    # print(cluster_means)
    # print("Using distance")
    return min(cluster_means)

def dot_score(word_emb, wb_embeddings, clusters, num_clusters):
    similarities = torch.matmul(wb_embeddings, word_emb)

    cluster_means = [0] * num_clusters
    cluster_counts = [0] * num_clusters
    for cluster, dist in zip(clusters, similarities):
        cluster_means[cluster] += dist
        cluster_counts[cluster] += 1

    cluster_means = [cluster_means[idx]/cluster_counts[idx] for idx in range(len(cluster_means))]
    # print("using dot product")
    return 1 / (max(cluster_means) + eps)
        

def dot_similarity(wb_embeddings, word_emb):
    similarities = torch.matmul(wb_embeddings, word_emb)
    return similarities

"""
Implement dotp, distp, BST, & other scoring functions below
"""
