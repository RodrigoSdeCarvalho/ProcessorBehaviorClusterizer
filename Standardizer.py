import numpy as np
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) #removes unnecessary numpy warning on terminal.

class Standardizer:
    def __init__(self):
        self.standardizer = StandardScaler()

    def standardize_dataset(self, dataset:list) -> np.array:
        np_dataset = np.array(dataset).tolist()
        standardized_dataset = self.standardizer.fit_transform(np.array(np_dataset))
        standardized_dataset = standardized_dataset.tolist()

        return standardized_dataset
