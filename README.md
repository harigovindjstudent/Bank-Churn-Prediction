# Bank Customer Churn Prediction

## Project Overview
This project focuses on predicting customer churn in the banking sector using machine learning techniques. Customer churn, or customer attrition, refers to when customers stop doing business with a bank. By identifying customers who are likely to churn, banks can take proactive measures to retain valuable customers.

## Dataset
The dataset contains various features about bank customers including:
- Demographic information (age, gender, geography)
- Banking relationship attributes (credit score, tenure, balance)
- Product usage (number of products, credit card status, active member status)
- Financial metrics (estimated salary)
- Target variable: 'Exited' (whether the customer has churned or not)

## Project Structure
```
├── config/                      # Configuration files
│   └── config.yaml             # Model and feature configuration
├── data/                        # Dataset files
│   └── Churn_Modelling.csv     # Raw customer data
├── models/                      # Saved model files
│   └── best_model.pkl          # Trained model
├── notebooks/                   # Jupyter notebooks
│   └── 02_churn_eda.ipynb      # Exploratory Data Analysis
├── src/                         # Source code
│   ├── data/                   # Data loading modules
│   │   └── data_loader.py      # Data loading and splitting
│   ├── features/               # Feature engineering modules
│   │   └── feature_engineering.py  # Feature creation and preprocessing
│   ├── models/                 # Model training modules
│   │   └── model_trainer.py    # Model training and evaluation
│   ├── utils/                  # Utility functions
│   └── main.py                 # Main execution script
├── analysis_insights.txt        # Documented insights and findings
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

## Analysis Highlights
- Comprehensive exploratory data analysis
- Feature correlation analysis
- Distribution analysis of key variables
- Target class distribution visualization
- Skewness analysis of numerical features

## Tools & Technologies
- Python
- Pandas for data manipulation
- Matplotlib & Seaborn for visualization
- Jupyter Notebooks for interactive development

## Current Progress
- Completed initial data exploration
- Analyzed feature distributions and correlations
- Identified key patterns in customer behavior
- Documented insights for feature engineering

## Next Steps
1. Feature engineering based on insights
2. Data preprocessing and scaling
3. Model development and training
4. Model evaluation and optimization
5. Results interpretation and recommendations

## Business Value
This project aims to help banks:
- Identify customers at risk of churning
- Understand factors contributing to customer churn
- Develop targeted retention strategies
- Reduce customer attrition rates
- Improve customer satisfaction and loyalty