"""
==========================================================
Intelligent Information Extraction System
AML23702 - Advanced Natural Language Processing Lab
==========================================================
"""

import os

from src.preprocess import TextPreprocessor
from src.pos_tagging import POSTagger
from src.ner import NamedEntityRecognizer
from src.relation_extraction import RelationExtractor
from src.event_extraction import EventExtractor
from src.temporal_ordering import TemporalOrdering
from src.visualization import Visualizer


def main():

    print("=" * 60)
    print(" Intelligent Information Extraction System ")
    print("=" * 60)

    dataset_path = "dataset/True.csv"

    if not os.path.exists(dataset_path):
        print("\nERROR: Dataset not found!")
        print("Place True.csv inside dataset folder.")
        return

    # ==========================================
    # PREPROCESSING
    # ==========================================

    print("\nLoading Dataset...")

    preprocessor = TextPreprocessor()

    df = preprocessor.load_dataset(dataset_path)

    text = preprocessor.combine_articles(df, number_of_articles=5)

    doc = preprocessor.process_text(text)

    print("✓ Dataset Loaded")

    # ==========================================
    # POS TAGGING
    # ==========================================

    print("\nPerforming POS Tagging...")

    pos = POSTagger()

    pos_df = pos.extract_pos(doc)

    pos.save_csv(pos_df)

    pos.statistics(pos_df)

    print("✓ POS Tagging Completed")

    # ==========================================
    # NAMED ENTITY RECOGNITION
    # ==========================================

    print("\nPerforming Named Entity Recognition...")

    ner = NamedEntityRecognizer()

    entity_df = ner.extract_entities(doc)

    ner.save_csv(entity_df)

    ner.statistics(entity_df)

    print("✓ NER Completed")

    # ==========================================
    # RELATION EXTRACTION
    # ==========================================

    print("\nExtracting Relations...")

    relation = RelationExtractor()

    relation_df = relation.extract_relations(doc)

    relation.save_csv(relation_df)

    relation.statistics(relation_df)

    print("✓ Relation Extraction Completed")

    # ==========================================
    # EVENT EXTRACTION
    # ==========================================

    print("\nExtracting Events...")

    events = EventExtractor()

    event_df = events.extract_events(doc)

    events.save_csv(event_df)

    events.statistics(event_df)

    print("✓ Event Extraction Completed")

    # ==========================================
    # TEMPORAL ORDERING
    # ==========================================

    print("\nGenerating Timeline...")

    timeline = TemporalOrdering()

    timeline_df = timeline.create_timeline(event_df)

    timeline.save_csv(timeline_df)

    timeline.statistics(timeline_df)

    print("✓ Timeline Generated")

    # ==========================================
    # VISUALIZATION
    # ==========================================

    print("\nGenerating Graphs...")

    visual = Visualizer()

    visual.pos_distribution(pos_df)

    visual.entity_distribution(entity_df)

    visual.top_entities(entity_df)

    visual.timeline_graph(timeline_df)

    print("✓ Graphs Saved")

    print("\n" + "=" * 60)
    print(" PROJECT COMPLETED SUCCESSFULLY ")
    print("=" * 60)

    print("\nGenerated Files:")

    print("\noutputs/")
    print("   pos_tags.csv")
    print("   entities.csv")
    print("   relations.csv")
    print("   events.csv")
    print("   timeline.csv")

    print("\nvisuals/")
    print("   pos_distribution.png")
    print("   entity_distribution.png")
    print("   top_entities.png")
    print("   timeline.png")


if __name__ == "__main__":
    main()