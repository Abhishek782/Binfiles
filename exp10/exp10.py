# import pandas as pd
# import numpy as np

# def calculate_distance(point1, point2):
#     return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

# def kmeans_clustering(data, num_clusters, max_iterations=100):
#     # Initialize centroids randomly
#     centroids = data.sample(n=num_clusters, random_state=42)
#     centroids = centroids.values

#     for _ in range(max_iterations):
#         # Assign each data point to the nearest centroid
#         data['cluster'] = data.apply(
#             lambda row: min(range(num_clusters), key=lambda i: calculate_distance(centroids[i], row)),
#             axis=1
#         )

#         # Update centroids based on the mean of assigned points
#         new_centroids = [data[data['cluster'] == i][['feature1', 'feature2']].mean().values for i in range(num_clusters)]

#         # Check for convergence
#         if np.array_equal(centroids, new_centroids):
#             break

#         centroids = new_centroids

#     return data, centroids

# # Read the CSV file
# input_file_path = 'data.csv'  # Replace with your CSV file path
# df = pd.read_csv(input_file_path)

# # Assuming your data has features 'feature1' and 'feature2', modify this according to your data
# features = df[['feature1', 'feature2']]

# # Get the number of clusters from the user
# num_clusters = int(input("Enter the number of clusters: "))

# # Perform K-means clustering
# result_df, cluster_centers = kmeans_clustering(features, num_clusters)

# # Print cluster centers
# print("\nCluster Centers:")
# for i, center in enumerate(cluster_centers):
#     print(f"Cluster {i + 1}: {center}")

# # Save the clustered data to a new CSV file if needed
# output_file_path = 'output_clustered_data.csv'
# result_df.to_csv(output_file_path, index=False)
# print(f"\nClustered data saved to {output_file_path}")


# # With 3 features
# import pandas as pd
# import numpy as np

# def calculate_distance(point1, point2):
#     return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

# def kmeans_clustering(data, num_clusters, max_iterations=100):
#     # Initialize centroids randomly
#     centroids = data.sample(n=num_clusters, random_state=42)
#     centroids = centroids.values

#     for _ in range(max_iterations):
#         # Assign each data point to the nearest centroid
#         data['cluster'] = data.apply(
#             lambda row: min(range(num_clusters), key=lambda i: calculate_distance(centroids[i], row)),
#             axis=1
#         )

#         # Update centroids based on the mean of assigned points
#         new_centroids = [data[data['cluster'] == i][['feature1', 'feature2', 'feature3']].mean().values for i in range(num_clusters)]

#         # Check for convergence
#         if np.array_equal(centroids, new_centroids):
#             break

#         centroids = new_centroids

#     return data, centroids

# # Read the CSV file
# input_file_path = 'data.csv'  # Replace with your CSV file path
# df = pd.read_csv(input_file_path)

# # Assuming your data has features 'feature1', 'feature2', and 'feature3', modify this according to your data
# features = df[['feature1', 'feature2', 'feature3']]

# # Get the number of clusters from the user
# num_clusters = int(input("Enter the number of clusters: "))

# # Perform K-means clustering
# result_df, cluster_centers = kmeans_clustering(features, num_clusters)

# # Print cluster centers
# print("\nCluster Centers:")
# for i, center in enumerate(cluster_centers):
#     print(f"Cluster {i + 1}: {center}")

# # Save the clustered data to a new CSV file if needed
# output_file_path = 'output_clustered_data.csv'
# result_df.to_csv(output_file_path, index=False)
# print(f"\nClustered data saved to {output_file_path}")


# import pandas as pd
# import numpy as np

# def calculate_distance(point1, point2):
#     return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

# def kmeans_clustering(data, num_clusters, max_iterations=100):
#     # Initialize centroids randomly
#     centroids = data.sample(n=num_clusters, random_state=42)
#     centroids = centroids.values

#     for _ in range(max_iterations):
#         # Assign each data point to the nearest centroid and calculate distances
#         data['cluster'] = data.apply(
#             lambda row: min(range(num_clusters), key=lambda i: calculate_distance(centroids[i], row)),
#             axis=1
#         )
#         data['distance_to_centroid'] = data.apply(
#             lambda row: calculate_distance(centroids[int(row['cluster'])], row),
#             axis=1
#         )

#         # Update centroids based on the mean of assigned points
#         new_centroids = [data[data['cluster'] == i][['feature1', 'feature2']].mean().values for i in range(num_clusters)]

#         # Check for convergence
#         if np.array_equal(centroids, new_centroids):
#             break

#         centroids = new_centroids

#     # Calculate cluster radius
#     cluster_radii = data.groupby('cluster')['distance_to_centroid'].max().to_dict()

#     return data, centroids, cluster_radii

# # Read the CSV file
# input_file_path = 'data.csv'  # Replace with your CSV file path
# df = pd.read_csv(input_file_path)

# # Assuming your data has features 'feature1' and 'feature2', modify this according to your data
# features = df[['feature1', 'feature2']]

# # Get the number of clusters from the user
# num_clusters = int(input("Enter the number of clusters: "))

# # Perform K-means clustering
# result_df, cluster_centers, cluster_radii = kmeans_clustering(features, num_clusters)

# # Print cluster centers and radii
# print("\nCluster Centers and Radii:")
# for i, (center, radius) in enumerate(zip(cluster_centers, cluster_radii.values())):
#     print(f"Cluster {i + 1}: Center {center}, Radius {radius:.2f}")

# # Save the clustered data to a new CSV file if needed
# output_file_path = 'output_clustered_data.csv'
# result_df.to_csv(output_file_path, index=False)
# print(f"\nClustered data saved to {output_file_path}")


# To get distance matrix as well
import pandas as pd
from scipy.spatial.distance import pdist, squareform

def compute_cluster_center(points):
    # Assuming 'points' is a DataFrame with columns representing multidimensional points
    center = points.mean(axis=0)
    return center

def compute_distances(points, cluster_center):
    # Compute distances between each point and the cluster center
    distances = pdist(points, metric='euclidean')
    # Convert the condensed distance matrix to a square matrix
    distance_matrix = squareform(distances)
    return distance_matrix

# Load data from CSV
file_path = 'input_data.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Assuming columns 'X' and 'Y' represent the coordinates of the points
points = data[['X', 'Y']]

# Compute the center of the cluster
cluster_center = compute_cluster_center(points)

# Save cluster center to CSV
cluster_center_df = pd.DataFrame(cluster_center).T  # Convert the series to a DataFrame
cluster_center_df.to_csv('cluster_center.csv', index=False)
print("Cluster Center CSV:")
print(cluster_center_df)

# Compute distances from each point to the cluster center
distance_matrix = compute_distances(points, cluster_center)

# Save distance matrix to CSV
distance_matrix_df = pd.DataFrame(distance_matrix, columns=data['ID'], index=data['ID'])
distance_matrix_df.to_csv('distance_matrix.csv')
print("\nDistance Matrix CSV:")
print(distance_matrix_df)
