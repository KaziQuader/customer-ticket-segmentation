import pandas as pd
from src.constants.label import label2id
import re
class TextProcessor:
    def __init__(self):
        pass

    def select_merge_drop(self, df, *args):
        df = df[list(args)]
        df.loc[:, 'text'] = (
            'Subject: ' + df['Ticket Subject'] + ' | ' +
            'Channel: ' + df['Ticket Channel'] + ' | ' + 
            'Description: ' + df['Ticket Description']
        )
        df = df.drop(['Ticket Subject', 'Ticket Description', 'Ticket Channel'], axis=1)
        return df

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)
        text = re.sub(r"\S+@\S+", "", text)
        text = re.sub(r"<.*?>", "", text)
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
    
    def transform(self, df, *args):
        df = self.select_merge_drop(df, *args)
        df['text'] = df['text'].apply(self.clean_text)
        return df


if __name__ == "__main__":
    df_raw = pd.read_csv('data/raw/customer_support_tickets.csv')
    df = df_raw.copy()

    processor = TextProcessor()
    df = processor.transform(df, 'Ticket Type', 'Ticket Subject', 'Ticket Description', 'Ticket Channel')
    df.to_csv('data/processed/processed.csv')
