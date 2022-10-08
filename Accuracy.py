from Clustering import Clustering

class Accuracy:
    @staticmethod
    def accuracy(clusters) -> float:
        """Checks if the clustering is right and returns its accuracy."""
        sum_accuracy_clusters = 0
        clusters = clusters
        num_clusters = len(clusters)

        for cluster in clusters:
            cluster_accuracy = Accuracy.__get_cluster_accuracy(cluster)
            sum_accuracy_clusters += cluster_accuracy

        accuracy = sum_accuracy_clusters / num_clusters

        return accuracy * 100

    @staticmethod
    def __get_cluster_accuracy(cluster) -> float:
        """Returns the accuracy of a cluster."""
        num_datapoints = len(cluster)
        cluster_ID = Accuracy.__get_cluster_ID(cluster)

        correctly_clustered_datapoint = 0 #calculate_cluster_accuracy
        for datapoint in cluster:
            id = datapoint[-1]
            if id == cluster_ID:
                correctly_clustered_datapoint += 1

        cluster_accuracy = correctly_clustered_datapoint / num_datapoints

        return cluster_accuracy * 100

    @staticmethod
    def __get_cluster_ID(cluster) -> int:
        """Returns the ID which represents a certain cluster."""
        IDs = Accuracy.__get_IDs(cluster)

        counter = 0
        cluster_ID = 0 #The most frequent element in IDs' list.

        for id in IDs: #Perhaps will have a high cost.
            curr_frequency = IDs.count(id)

            if curr_frequency > len(IDs)/2:
                return id 

            if(curr_frequency > counter):
                counter = curr_frequency
                cluster_ID = id

        return cluster_ID

    @staticmethod
    def __get_IDs(cluster) -> list:
        """Returns a list of all the IDs of the datapoints in a cluster."""
        IDs = []

        for datapoint in cluster:
            id = datapoint[-1] #or index == 6
            IDs.append(id)

        return IDs

    #methods to calculate the accuracy of the algorithm (clustered-nonClustered).
    @staticmethod
    def capture_accuracy(original_dataset, centroids, max_radius, dataset_dimensions) -> float:
        """Checks how many datapoints would be clustered given the centroids after the clustization and returns the accuracy in percentage. Is 100% accurate only if no datapoint has been removed."""
        dataset = original_dataset
        centroids = centroids
        max_radius = max_radius

        captured = 0
        for datapoint in dataset:
            for centroid in centroids:
                if Accuracy.__bind(datapoint, centroid, max_radius, dataset_dimensions):
                    captured += 1
                    break

        num_datapoints = len(dataset)

        accuracy = (float(captured / num_datapoints)) * 100

        return accuracy

    @staticmethod
    def __bind(datapoint_x, datapoint_y, threshold, dataset_dimensions) -> bool:
        """Checks if the distance between the datapoints x and y exceeds a binding threshold."""
        dist = Clustering.euclidean_distance(datapoint_x, datapoint_y, dataset_dimensions)

        if dist <= threshold:
            return True
        else:
            return False

    @staticmethod
    def rate_of_clusterization(original_dataset, clusters) -> float:
        """calculates the % of clustered dps by dividing the number of clustered datapoints by the number of datapoints in the dataset."""
        total = len(original_dataset)
        clustered = 0

        for cluster in clusters:
            clustered += len(cluster)

        rate = clustered / total * 100
        return round(rate, 2)
