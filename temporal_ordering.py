"""
==========================================================
temporal_ordering.py
----------------------------------------------------------
Temporal Ordering Module
Creates a timeline of detected events.
==========================================================
"""

import os
import pandas as pd


class TemporalOrdering:

    def __init__(self):
        pass

    def create_timeline(self, event_df):

        timeline = event_df.copy()

        # Replace empty dates with Unknown
        timeline["Date"] = timeline["Date"].replace("", "Unknown")
        timeline["Date"] = timeline["Date"].fillna("Unknown")

        # Sort alphabetically (simple timeline)
        timeline = timeline.sort_values(by="Date")

        return timeline

    def save_csv(self, dataframe):

        os.makedirs("outputs", exist_ok=True)

        dataframe.to_csv(
            "outputs/timeline.csv",
            index=False
        )

        print("\n✓ Timeline saved to outputs/timeline.csv")

    def show_timeline(self, dataframe, n=20):

        print("\n========== EVENT TIMELINE ==========\n")

        print(dataframe.head(n))

        print("\n====================================")

    def statistics(self, dataframe):

        print("\n========== TIMELINE SUMMARY ==========\n")

        print("Total Timeline Entries :", len(dataframe))

        print("\n======================================")