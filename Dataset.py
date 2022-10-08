from Standardizer import Standardizer
from Path import Path
import pandas as pd

class Dataset:
    def __init__(self, dataset_file_name:str):
        self.dataset_standardizer = Standardizer()
        self.dataset_path = Path.get_dataset_path(dataset_file_name)

    def csv_to_list(self, dataset_columns) -> list:
        """Transforms the csv format file into a python list"""
        list_dataset = pd.read_csv(self.dataset_path)
        list_dataset = list_dataset.iloc[:,0:dataset_columns].values.tolist()
        
        return list_dataset
