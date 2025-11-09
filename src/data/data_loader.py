import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    def __init__(self, config_path):
        """Initialize DataLoader with configuration."""
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
    def load_data(self):
        """Load raw data from specified path."""
        try:
            logger.info(f"Loading data from {self.config['data']['raw_data_path']}")
            df = pd.read_csv(self.config['data']['raw_data_path'])
            return df
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def split_data(self, df, target_col='Exited'):
        """Split data into training and testing sets."""
        try:
            X = df.drop([target_col, 'RowNumber', 'CustomerId', 'Surname'], axis=1)
            y = df[target_col]
            
            X_train, X_test, y_train, y_test = train_test_split(
                X, y,
                test_size=self.config['data']['test_size'],
                random_state=self.config['data']['random_state']
            )
            
            logger.info("Data split completed successfully")
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logger.error(f"Error splitting data: {str(e)}")
            raise