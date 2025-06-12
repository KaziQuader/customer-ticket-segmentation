import pandas as pd
from src.constants.label import label2id

# Merge Columns
def merge_and_drop(df, *args):
    print(args)

# Clean text
def clean_text():
    pass

def preprocess(): 
    df_raw = pd.read_csv('data/raw/customer_support_tickets.csv')
    df = df_raw.copy()

    merge_and_drop(df, 'text', 'Ticket Type', 'Ticket Subject', 'Ticket Description', 'Ticket Channel')


if __name__ == "__main__":
    preprocess()

