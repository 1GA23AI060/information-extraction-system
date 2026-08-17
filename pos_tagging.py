"""
==========================================================
pos_tagging.py
----------------------------------------------------------
Performs Part-of-Speech Tagging
==========================================================
"""

import os
import pandas as pd


class POSTagger:

    def __init__(self):
        pass

    def extract_pos(self, doc):

        pos_data = []

        for token in doc:

            if token.is_space:
                continue

            pos_data.append({
                "Word": token.text,
                "Lemma": token.lemma_,
                "POS": token.pos_,
                "Tag": token.tag_,
                "Dependency": token.dep_
            })

        pos_df = pd.DataFrame(pos_data)

        return pos_df

    def save_csv(self, dataframe):

        os.makedirs("outputs", exist_ok=True)

        dataframe.to_csv(
            "outputs/pos_tags.csv",
            index=False
        )

        print("\n✓ POS Tags saved to outputs/pos_tags.csv")

    def statistics(self, dataframe):

        print("\n========== POS Statistics ==========\n")

        print(dataframe["POS"].value_counts())

        print("\n====================================")

    def top_words(self, dataframe, n=20):

        print("\n========== Sample POS Tags ==========\n")

        print(dataframe.head(n))

        print("\n====================================")