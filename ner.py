"""
==========================================================
ner.py
----------------------------------------------------------
Named Entity Recognition Module
==========================================================
"""

import os
import pandas as pd


class NamedEntityRecognizer:

    def __init__(self):
        pass

    def extract_entities(self, doc):

        entities = []

        for ent in doc.ents:

            entities.append({
                "Entity": ent.text,
                "Label": ent.label_,
                "Start": ent.start_char,
                "End": ent.end_char
            })

        entity_df = pd.DataFrame(entities)

        return entity_df

    def save_csv(self, dataframe):

        os.makedirs("outputs", exist_ok=True)

        dataframe.to_csv(
            "outputs/entities.csv",
            index=False
        )

        print("\n✓ Entities saved to outputs/entities.csv")

    def statistics(self, dataframe):

        print("\n========== ENTITY STATISTICS ==========\n")

        print(dataframe["Label"].value_counts())

        print("\n=======================================\n")

    def show_entities(self, dataframe, n=20):

        print("\n========== SAMPLE ENTITIES ==========\n")

        print(dataframe.head(n))

        print("\n=====================================\n")

    def filter_person(self, dataframe):

        return dataframe[dataframe["Label"] == "PERSON"]

    def filter_org(self, dataframe):

        return dataframe[dataframe["Label"] == "ORG"]

    def filter_gpe(self, dataframe):

        return dataframe[dataframe["Label"] == "GPE"]

    def filter_date(self, dataframe):

        return dataframe[dataframe["Label"] == "DATE"]