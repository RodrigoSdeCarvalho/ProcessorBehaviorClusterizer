import math
import numpy as np
from Dataset import Dataset

class Clustering:
    def __init__(self,  centroids_indexes:list, dataset_file_name:str, max_radius:int, min_in_cluster:int, dataset_dimensions:int ) -> None:
        """Receives a dataset, the centroids, the maximum value for the centroids' cluster
           and creates an empty list to store the clusters.
        """
        self.__dataset = Dataset(dataset_file_name).csv_to_list(7)
        self.__original_dataset = Dataset(dataset_file_name).csv_to_list(7) #Not affected by outlier remotion. Used for accuracy calculations.
        self.__max_radius = max_radius
        self.__dataset_dimensions = dataset_dimensions
        self.__min_in_cluster = min_in_cluster
        self.__accuracy = -1
        self.__centroids = self.generate_centroids_attribute(centroids_indexes)
        self.__clusters = self.generate_clusters_attribute()

        self.__data_point_already_in_cluster = [False]*len(self.__dataset) #keeps a track on whether or not a point has been clustered.

    def generate_centroids_attribute(self, centroids_indexes) -> list:
        centroids = []
        if centroids_indexes == []:
            centroids.append(self.__dataset[0])
        else:
            for index in centroids_indexes:
                centroids.append(self.__dataset[index])
        
        return centroids

    def generate_clusters_attribute(self) -> list:
        clusters = []
        for centroid in self.__centroids:
            new_centroid = [centroid]
            clusters.append(new_centroid) 

        return clusters     

    @property    
    def dataset(self):
        return self.__dataset
    
    @property
    def original_dataset(self):
        return self.__original_dataset

    @property    
    def centroids(self):
        return self.__centroids    

    @property
    def clusters(self):
        return self.__clusters

    @property    
    def max_radius(self):
        return self.__max_radius

    @property
    def dataset_dimensions(self):
        return self.__dataset_dimensions

    @property
    def min_in_cluster(self):
        return self.__min_in_cluster

    @property
    def accuracy(self):
        return self.__accuracy

    def new_data_point(self, data_point: list) -> None:
        """Creates a new data point in the data set."""
        self.__dataset.append(data_point)

    def new_cluster(self, centroid: list) -> None:
        """Creates a new cluster and defines its centroid."""
        new_cluster = [centroid]
        self.centroids.append(centroid)
        self.clusters.append(new_cluster)

    @staticmethod
    def euclidean_distance(data_point1: list, data_point2: list, dataset_dimensions) -> float:
        """Calculates and returns the euclidean distance between two 
        given data points
        """
        num_coordinates = dataset_dimensions

        distance = 0
        for i in range(num_coordinates):
            
            distance += ((data_point1[i] - data_point2[i]) ** 2)
        distance = math.sqrt(distance)

        return distance

    def datapoint_fits_in_cluster(self, data_point: list, centroid: list) -> bool:
        """Determines if a data point belongs to a cluster, given its centroid."""
        distance = self.euclidean_distance(data_point, centroid, self.dataset_dimensions)

        if distance <= self.max_radius:
            return True
        else:
            return False

    def show_clusters(self) -> None:
        """Shows all the clusters in the terminal."""
        n = 1
        for cluster in self.clusters:
            print(f'cluster {n}: {cluster}')
            n += 1

    def show_number_of_clusters(self) -> int:
        """Returns the numbers of clusters calculated by the algorithm."""
        number_of_clusters = len(self.clusters)
        print(number_of_clusters)

        return number_of_clusters

    #methods used to remove outliers
    def get_data_dimensions(self) -> list:
        """Gets the data points dimensions and separates them in lists.
           It returns an array with all the data dimensions."""
        dataset = self.dataset

        data_0 = []
        data_1 = []
        data_2 = []
        data_3 = []
        data_4 = []
        data_5 = []
        data_ID = []

        for data_point in dataset:
            data_0.append(data_point[0])
            data_1.append(data_point[1])
            data_2.append(data_point[2])
            data_3.append(data_point[3])
            data_4.append(data_point[4])
            data_5.append(data_point[5])
            data_ID.append(data_point[6])

        data_dimensions = [data_0, data_1, data_2, data_3, data_4, data_5,data_ID]

        return data_dimensions

    def to_dataset(self, data_dimensions) -> list:
        """Receives a data_dimensions array and converts it to dataset."""
        dataset = []

        for index_datapoint in range(len(data_dimensions[0])):

            datapoint = [data_dimensions[0][index_datapoint],
                         data_dimensions[1][index_datapoint],
                         data_dimensions[2][index_datapoint],
                         data_dimensions[3][index_datapoint],
                         data_dimensions[4][index_datapoint],
                         data_dimensions[5][index_datapoint],
                         data_dimensions[6][index_datapoint]]
            dataset.append(datapoint)

        return dataset

    def remove_outliers(self) -> list:
        """Removes outliers in the dataset. And returns the dataset without outliers"""
        data_dimensions = self.get_data_dimensions()
        data_dimensions = np.array(data_dimensions)

        indexes_to_remove = []
        for index_axis, axis in enumerate(data_dimensions[0:6]):

            data_std = np.std(data_dimensions[index_axis])
            data_mean = np.mean(data_dimensions[index_axis])

            for index_value, value in enumerate(axis):
                if not (value <= data_mean + 3*data_std):
                    indexes_to_remove.append(index_value)

        data_dimensions = data_dimensions.tolist()
        aux_data_dimensions = self.get_data_dimensions()
        indexes_to_remove = list(set(indexes_to_remove))

        for index in indexes_to_remove:
            data_dimensions[0].remove(aux_data_dimensions[0][index])
            data_dimensions[1].remove(aux_data_dimensions[1][index])
            data_dimensions[2].remove(aux_data_dimensions[2][index])
            data_dimensions[3].remove(aux_data_dimensions[3][index])
            data_dimensions[4].remove(aux_data_dimensions[4][index])
            data_dimensions[5].remove(aux_data_dimensions[5][index])
            data_dimensions[6].remove(aux_data_dimensions[6][index])

        dataset = self.to_dataset(data_dimensions)
        self.dataset = dataset 
        
        return self.dataset

    #methods for running the algorithm
    def __data_point_fits_in_cluster_and_isnt_clustered(self, data_point, index_data_point, centroid):
        return (self.datapoint_fits_in_cluster(data_point, centroid) and (not self.__data_point_already_in_cluster[index_data_point]))

    def __include_data_point_in_cluster(self, data_point, index_data_point, index_centroid):
        self.clusters[index_centroid].append(data_point)
        self.__data_point_already_in_cluster[index_data_point] = True #In case of a bug, change this cause it may be changing only locally.

    def __data_point_doesnt_fit_in_any_cluster(self, index_data_point):
        return not (self.__data_point_already_in_cluster[index_data_point])

    def __clustering_algorithm(self, dataset_list, centroids):
        for index_data_point, data_point in enumerate(dataset_list):
            for index_centroid, centroid in enumerate(centroids):
                if self.__data_point_fits_in_cluster_and_isnt_clustered(data_point, index_data_point, centroid):
                    self.__include_data_point_in_cluster(data_point, index_data_point, index_centroid)

            if self.__data_point_doesnt_fit_in_any_cluster(index_data_point):
                self.new_cluster(data_point)

        return self.clusters

    def start(self) -> list:
        """Starts the clustering algorithm and returns the clusters."""
        dataset_list = self.dataset
        centroids = self.centroids
        clusters = self.__clustering_algorithm(dataset_list, centroids)

        return clusters

    def start_min(self) -> list:
        """Starts the clustering algorithm and returns the clusters
        that have less or an equal number of members in comparison to
        the maximum number in a cluster."""
        self.start()

        clusters = self.clusters
        min = self.min_in_cluster
        new_clusters = []
        new_centroids = []

        for cluster in clusters: #Clean
            if len(cluster) >= min:
                new_clusters.append(cluster)
                new_centroids.append(cluster[0])

        self.__clusters = new_clusters
        self.__centroids = new_centroids

        return self.__clusters

    def start_without_outliers(self) -> None:
        """Removes the outliers and runs the algorithm."""
        self.remove_outliers()
        self.start()
        
    def start_min_and_without_outliers(self) -> None:
        """Runs the full clustering algorithm, without outliers and with a minimum
            number of members for a cluster."""
        self.remove_outliers()
        self.start_min()
