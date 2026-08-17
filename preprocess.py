"""
==========================================================
preprocess.py
----------------------------------------------------------
Loads dataset and preprocesses the text.
==========================================================
"""

import os
import pandas as pd
import spacy


class TextPreprocessor:

    def __init__(self):
        """Load spaCy model."""
        self.nlp = spacy.load("en_core_web_sm")

    def load_dataset(self, path):
        """Load CSV dataset."""

        if not os.path.exists(path):
            raise FileNotFoundError(f"\nDataset not found:\n{path}")

        df = pd.read_csv(path)

        print(f"\nDataset Loaded Successfully")
        print(f"Rows : {len(df)}")
        print(f"Columns : {len(df.columns)}")

        return df

    def clean_text(self, text):

        if pd.isna(text):
            return ""

        text = str(text)

        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
        text = text.replace("  ", " ")

        return text

    def combine_articles(self, dataframe, number_of_articles=5):

        combined = ""

        for article in dataframe["text"].head(number_of_articles):
            combined += self.clean_text(article) + " "

        return combined

    def process_text(self, text):

        doc = self.nlp(text)

        return doc