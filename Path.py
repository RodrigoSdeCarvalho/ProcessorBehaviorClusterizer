import os

class Path:
    @staticmethod
    def get_dataset_path(file_name:str) -> str:
        """Returns the path of the dataset, which must be in the data folder, given the file's name."""
        base_path = os.path.join(os.getcwd())
        dataset_path = f'{base_path}/data/{file_name}'
        dataset_path = os.path.join(dataset_path)
        
        return dataset_path

    @staticmethod
    def get_report_path() -> str:
        """Returns the reports' folder path."""
        base_path = os.path.join(os.getcwd())
        report_path = f'{base_path}/reports/'
        report_path = os.path.join(report_path)
        
        return report_path
