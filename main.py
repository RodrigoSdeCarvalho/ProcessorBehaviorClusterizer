from Clustering import Clustering
from ReportGenerator import ReportGenerator
from Path import Path

if __name__ == "__main__":  
    centroids = []
    dataset_file_name = "dataset.csv"
    max_radius = 0.10 
    min_members_cluster = 3
    dataset_dimensions = 6

    clustering = Clustering(centroids, dataset_file_name, max_radius, min_members_cluster, dataset_dimensions)
    clustering.start()

    report_path = Path.get_report_path()
    ReportGenerator.generate_report("Test_Report", report_path, clustering)
