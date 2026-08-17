"""
==========================================================
relation_extraction.py
----------------------------------------------------------
Extract Subject - Verb - Object Relations
==========================================================
"""

import os
import pandas as pd


class RelationExtractor:

    def __init__(self):
        pass

    def extract_relations(self, doc):

        relations = []

        for sent in doc.sents:

            subject = ""
            relation = ""
            obj = ""

            for token in sent:

                # Subject
                if token.dep_ in ("nsubj", "nsubjpass"):
                    subject = token.text

                # Verb
                if token.pos_ == "VERB":
                    relation = token.lemma_

                # Object
                if token.dep_ in ("dobj", "pobj", "attr", "obj"):
                    obj = token.text

            if subject and relation and obj:
                relations.append({
                    "Subject": subject,
                    "Relation": relation,
                    "Object": obj
                })

        relation_df = pd.DataFrame(relations)

        return relation_df

    def save_csv(self, dataframe):

        os.makedirs("outputs", exist_ok=True)

        dataframe.to_csv(
            "outputs/relations.csv",
            index=False
        )

        print("\n✓ Relations saved to outputs/relations.csv")

    def statistics(self, dataframe):

        print("\n========== RELATION STATISTICS ==========\n")

        print("Total Relations :", len(dataframe))

        print("\n=========================================\n")

    def show_relations(self, dataframe, n=20):

        print("\n========== SAMPLE RELATIONS ==========\n")

        print(dataframe.head(n))

        print("\n======================================\n")