import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Config
DATASET = "suraj520/customer-support-ticket-dataset"  # e.g., "rounakbanik/the-movies-dataset"
OUTPUT_DIR = "data/raw"

def download_kaggle_dataset(dataset: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    print(f"Downloading dataset: {dataset}")
    api.dataset_download_files(dataset, path=output_dir, unzip=True)
    print(f"Dataset downloaded and extracted to: {output_dir}")

if __name__ == "__main__":
    download_kaggle_dataset(DATASET, OUTPUT_DIR)