#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:09:30 2023

@author: temuuleu
"""

import importlib
import os 
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def check_dependencies(dependencies):
    for dependency in dependencies:
        try:
            importlib.import_module(dependency)
            print(f"Successfully imported {dependency}")
        except ImportError:
            print(f"Dependency {dependency} is missing. Please install with pip:")
            print(f"pip install {dependency}")

# Example usage
dependencies = ["numpy","pandas","sentence_transformers","sklearn","matplotlib"]
check_dependencies(dependencies)     

import pandas as pd
import matplotlib.pyplot as plt

#pip install sentence_transformers
from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.cluster import KMeans

from sklearn.metrics import silhouette_score

def generate_embeddings(sentences_list, model):
    tokens = model.encode(sentences_list)
    
    sim = np.zeros((len(sentences_list), len(sentences_list)))
    for i in range(len(sentences_list)):
        sim[i:, i] = np.round(cos_sim(tokens[i], tokens[i:]), 2)

    return tokens,sim

# def cluster_words(embeddings, n_clusters=5):
#     kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(embeddings)
#     return kmeans.labels_, kmeans.cluster_centers_

def cluster_words(embeddings, n_clusters):
    kmeans_model = KMeans(n_clusters=n_clusters, n_init=10)  # Add n_init parameter
    cluster_labels = kmeans_model.fit_predict(embeddings)
    cluster_centers = kmeans_model.cluster_centers_

    return cluster_labels, cluster_centers



def find_optimal_clusters(embeddings, max_clusters=10):
    inertia_values = []
    cluster_range = range(1, max_clusters+1)

    for n_clusters in cluster_range:
        kmeans = KMeans(n_clusters=n_clusters).fit(embeddings)
        inertia_values.append(kmeans.inertia_)

    optimal_clusters = None  # Define optimal_clusters initially

    def submit_cluster_number():
        nonlocal optimal_clusters  # Declare optimal_clusters as nonlocal variable
        try:
            optimal_clusters = int(entry.get())
            root.quit()
        except ValueError:
            messagebox.showerror("Error", "Please enter an integer value for the number of clusters.")

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Optimal Cluster Size")

    fig = Figure(figsize=(6, 4), dpi=100)
    plt = fig.add_subplot(1, 1, 1)
    plt.plot(cluster_range, inertia_values, 'bo-')
    plt.set_xlabel('Number of Clusters (k)')
    plt.set_ylabel('Inertia')
    plt.set_title("Elbow Method")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    label = tk.Label(root, text="Enter the optimal number of clusters from the elbow plot:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    button = tk.Button(root, text="Submit", command=submit_cluster_number)
    button.pack(pady=10)

    root.mainloop()
    root.destroy()

    return optimal_clusters


# Read files and combine content
def read_files_and_combine_content(txt_dirs_list):
    all_text = ""
    for txt_path in txt_dirs_list:
        with open(txt_path, 'r') as file:
            text = file.read()
            all_text += text
    return all_text


path_to_txt = "text"
txt_dirs_list  = [os.path.join(path_to_txt, d) for d in os.listdir(path_to_txt) if "txt" in d]
print("reading the text")
all_text  =    read_files_and_combine_content(txt_dirs_list)

#remove small text
sentences_list = [f.strip() for f in all_text.split(".") if len(f) > 5]
#load the model
print(f"loading model..")
model = SentenceTransformer('bert-base-nli-mean-tokens')
print(f"loading model finisched")

print(f"generating embedings")
tokens,sim = generate_embeddings(sentences_list, model)  
print(f"created tokens: {len(tokens)}")
#find optimal kmeans
n_clusters = find_optimal_clusters(tokens)

print(f"cperforming kmeans with k={n_clusters}")
# Perform K-Means clustering on the embeddings
cluster_labels, cluster_centers = cluster_words(tokens, n_clusters)


# Group sentences by their cluster labels
clusters = {}
for i, label in enumerate(cluster_labels):
    if label not in clusters:
        clusters[label] = []
    clusters[label].append(sentences_list[i])

print("creating the dataframe")
clusters_df = pd.DataFrame({'Cluster': cluster_labels, 'Sentence': sentences_list})
clusters_df = clusters_df.sort_values(by=["Cluster"]).reset_index(drop=True)

print(f"saving the clusters to excel clusters.xlsx")
clusters_df.to_excel("clusters.xlsx")





