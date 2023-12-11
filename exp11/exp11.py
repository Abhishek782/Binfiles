import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load data from CSV
file_path = 'input_data.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Select relevant features for clustering (X and Y coordinates)
coordinates = data[['X', 'Y']].values

# Standardize the features
scaler = StandardScaler()
coordinates_scaled = scaler.fit_transform(coordinates)

# Perform hierarchical clustering
# 'n_clusters' is the number of clusters you want to obtain
# 'linkage' is set to 'single' for single linkage method
agg_clustering = AgglomerativeClustering(n_clusters=1, linkage='single')
clusters = agg_clustering.fit_predict(coordinates_scaled)

# Plot the dendrogram
linkage_matrix = linkage(coordinates_scaled, method='single')
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

# Add the cluster labels to the original data
data['Cluster'] = clusters

# Print the resulting clusters
# print("Resulting Clusters:")
# print(data[['ID', 'Cluster']])
