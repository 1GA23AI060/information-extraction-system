"""
==========================================================
visualization.py
----------------------------------------------------------
Creates charts for NLP outputs
==========================================================
"""

import os
import matplotlib.pyplot as plt


class Visualizer:

    def __init__(self):

        os.makedirs("visuals", exist_ok=True)

    # -----------------------------------------
    # POS Distribution
    # -----------------------------------------

    def pos_distribution(self, pos_df):

        plt.figure(figsize=(10,6))

        pos_df["POS"].value_counts().plot(kind="bar")

        plt.title("Part of Speech Distribution")
        plt.xlabel("POS Tags")
        plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig("visuals/pos_distribution.png")

        plt.close()

        print("✓ POS Distribution Graph Saved")


    # -----------------------------------------
    # Entity Distribution
    # -----------------------------------------

    def entity_distribution(self, entity_df):

        plt.figure(figsize=(10,6))

        entity_df["Label"].value_counts().plot(kind="bar")

        plt.title("Named Entity Distribution")
        plt.xlabel("Entity Type")
        plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig("visuals/entity_distribution.png")

        plt.close()

        print("✓ Entity Distribution Graph Saved")


    # -----------------------------------------
    # Top 10 Named Entities
    # -----------------------------------------

    def top_entities(self, entity_df):

        plt.figure(figsize=(12,6))

        entity_df["Entity"].value_counts().head(10).plot(kind="bar")

        plt.title("Top 10 Named Entities")
        plt.xlabel("Entity")
        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig("visuals/top_entities.png")

        plt.close()

        print("✓ Top Entities Graph Saved")


    # -----------------------------------------
    # Timeline Graph
    # -----------------------------------------

    def timeline_graph(self, timeline_df):

        plt.figure(figsize=(12,6))

        timeline_df["Date"].value_counts().plot(kind="bar")

        plt.title("Timeline Distribution")
        plt.xlabel("Date")
        plt.ylabel("Events")

        plt.tight_layout()

        plt.savefig("visuals/timeline.png")

        plt.close()

        print("✓ Timeline Graph Saved")