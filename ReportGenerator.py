import os
from Clustering import Clustering
from Accuracy import Accuracy

class ReportGenerator:
    @staticmethod
    def generate_report(txt_name:str, folder_path:str, clustering_obj: Clustering) -> None:
        """Creates a txt file and saves the clusters in it."""
        path = f"{folder_path}/{txt_name}.txt"
        path = os.path.join(path)
        
        txt_cluster = open(path, "w+")
        number_of_clusters = len(clustering_obj.clusters)

        txt_cluster.write(f'{txt_name}: \n'
                          '\n'
                          f'centroids: {clustering_obj.centroids} \n' 
                          '\n'
                          f'radius: {clustering_obj.max_radius} \n'
                          '\n'
                          f'minimum number of members in a cluster (if start_min was used): {clustering_obj.min_in_cluster} \n'
                          '\n'
                          f'accuracy (with the final set of centroids): {round(Accuracy.capture_accuracy(clustering_obj.original_dataset, clustering_obj.centroids, clustering_obj.max_radius, clustering_obj.dataset_dimensions), 2)} \n'
                          '\n'
                          f'rate of clusterization (clustered datapoints): {Accuracy.rate_of_clusterization(clustering_obj.original_dataset, clustering_obj.clusters)} \n'
                          '\n'
                          f'number of clusters: {number_of_clusters} \n'
                          '\n')

        n = 1
        for cluster in clustering_obj.clusters: 
            txt_cluster.write(f'cluster {n}: {cluster}')
            n += 1

            txt_cluster.write('\n') #Blank line.
            txt_cluster.write('\n')

        txt_cluster.close()
