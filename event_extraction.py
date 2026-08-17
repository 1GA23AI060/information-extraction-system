"""
==========================================================
event_extraction.py
----------------------------------------------------------
Extract Events from News Articles
==========================================================
"""

import os
import pandas as pd


class EventExtractor:

    def __init__(self):
        pass

    def extract_events(self, doc):

        events = []

        for sent in doc.sents:

            event = ""
            person = ""
            location = ""
            date = ""

            # Find the main event (root verb)
            for token in sent:

                if token.dep_ == "ROOT" and token.pos_ == "VERB":
                    event = token.lemma_

            # Extract entities in the sentence
            for ent in sent.ents:

                if ent.label_ == "PERSON":
                    person = ent.text

                elif ent.label_ == "GPE":
                    location = ent.text

                elif ent.label_ == "DATE":
                    date = ent.text

            if event:
                events.append({
                    "Event": event,
                    "Person": person,
                    "Location": location,
                    "Date": date
                })

        event_df = pd.DataFrame(events)

        return event_df

    def save_csv(self, dataframe):

        os.makedirs("outputs", exist_ok=True)

        dataframe.to_csv(
            "outputs/events.csv",
            index=False
        )

        print("\n✓ Events saved to outputs/events.csv")

    def statistics(self, dataframe):

        print("\n========== EVENT STATISTICS ==========\n")

        print("Total Events :", len(dataframe))

        print("\n======================================")

    def show_events(self, dataframe, n=20):

        print("\n========== SAMPLE EVENTS ==========\n")

        print(dataframe.head(n))

        print("\n===================================")