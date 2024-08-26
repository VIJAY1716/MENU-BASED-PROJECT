import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def process_data(file_path, save_path=None):
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully. Shape: {df.shape}")
        
        # Handle missing values
        df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill numerical NaNs with mean
        df.fillna(df.mode().iloc[0], inplace=True)  # Fill categorical NaNs with mode
        print("Missing values handled.")

        # Encode categorical features
        for column in df.select_dtypes(include=['object']).columns:
            df[column] = LabelEncoder().fit_transform(df[column])
        print("Categorical features encoded.")
        
        # Standardize numerical features
        numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
        scaler = StandardScaler()
        df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
        print("Numerical features standardized.")
        
        # Save the processed dataset if a save path is provided
        if save_path:
            df.to_csv(save_path, index=False)
            print(f"Processed dataset saved to: {save_path}")
        
        return df

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'V:/OneDrive/Desktop/menu_based_project/ml/dataset.csv'
save_path = 'V:/OneDrive/Desktop/menu_based_project/ml/processed_dataset.csv'
processed_data = process_data(file_path, save_path)
if processed_data is not None:
    print(processed_data.head())
