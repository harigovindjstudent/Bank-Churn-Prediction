import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FeatureEngineering:
    def __init__(self, config_path):
        """Initialize feature engineering with configuration."""
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.label_encoders = {}
        self.scaler = StandardScaler()
        
    def preprocess_features(self, df, is_training=True):
        """Preprocess features including encoding and scaling."""
        try:
            df_processed = df.copy()
            
            # Handle categorical features
            for feature in self.config['feature_engineering']['categorical_features']:
                if is_training:
                    self.label_encoders[feature] = LabelEncoder()
                    df_processed[feature] = self.label_encoders[feature].fit_transform(df_processed[feature])
                else:
                    df_processed[feature] = self.label_encoders[feature].transform(df_processed[feature])
            
            # Scale numerical features
            numerical_features = self.config['feature_engineering']['numerical_features']
            if is_training:
                df_processed[numerical_features] = self.scaler.fit_transform(df_processed[numerical_features])
            else:
                df_processed[numerical_features] = self.scaler.transform(df_processed[numerical_features])
            
            logger.info("Feature preprocessing completed successfully")
            return df_processed
            
        except Exception as e:
            logger.error(f"Error in feature preprocessing: {str(e)}")
            raise
    
    def create_features(self, df):
        """Create new features based on domain knowledge."""
        try:
            df_new = df.copy()
            
            # Example feature: Balance per product
            df_new['BalancePerProduct'] = df_new['Balance'] / (df_new['NumOfProducts'] + 1)
            
            # Example feature: Customer engagement score
            df_new['EngagementScore'] = df_new['IsActiveMember'] * 0.5 + df_new['HasCrCard'] * 0.3 + \
                                      (df_new['NumOfProducts'] / 4) * 0.2
            
            logger.info("Feature creation completed successfully")
            return df_new
            
        except Exception as e:
            logger.error(f"Error in feature creation: {str(e)}")
            raise