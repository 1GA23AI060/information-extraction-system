import streamlit as st
import pandas as pd
import os
import plotly.express as px

from src.preprocess import TextPreprocessor
from src.pos_tagging import POSTagger
from src.ner import NamedEntityRecognizer
from src.relation_extraction import RelationExtractor
from src.event_extraction import EventExtractor
from src.temporal_ordering import TemporalOrdering
from src.visualization import Visualizer


# -----------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------

st.set_page_config(
    page_title="Information Extraction System",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#1E88E5;
    font-size:45px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:20px;
}

.metric-box{
    background-color:#F5F5F5;
    padding:15px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------

st.markdown(
    "<div class='main-title'>📄 Intelligent Information Extraction System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Advanced NLP Mini Project</div>",
    unsafe_allow_html=True
)

st.write("")

# -----------------------------------------------------
# SIDEBAR
# -----------------------------------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Menu",
    [
        "📊 Dashboard"
    ]
)

if page == "📊 Dashboard":

    st.header("Upload Dataset")

    uploaded_file = st.file_uploader(
        "Choose Fake.csv or True.csv",
        type=["csv"]
    )

    if uploaded_file is not None:

        os.makedirs("dataset", exist_ok=True)

        dataset_path = os.path.join(
            "dataset",
            uploaded_file.name
        )

        with open(dataset_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Dataset Uploaded Successfully!")

        df = pd.read_csv(dataset_path)

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Articles",
            len(df)
        )

        col2.metric(
            "Columns",
            len(df.columns)
        )

        total_words = int(
            df["text"]
            .astype(str)
            .str.split()
            .str.len()
            .sum()
        )

        col3.metric(
            "Words",
            total_words
        )

        total_characters = int(
            df["text"]
            .astype(str)
            .str.len()
            .sum()
        )

        col4.metric(
            "Characters",
            total_characters
        )

        st.write("")

        analyze = st.button(
            "🚀 Analyze Dataset",
            use_container_width=True
        )
        if analyze:

            progress = st.progress(0)

            status = st.empty()

            # ------------------------------
            # PREPROCESSING
            # ------------------------------

            status.info("📖 Loading Dataset...")

            preprocessor = TextPreprocessor()

            df = preprocessor.load_dataset(dataset_path)

            text = preprocessor.combine_articles(
                df,
                number_of_articles=10
            )

            doc = preprocessor.process_text(text)

            progress.progress(15)

            # ------------------------------
            # POS TAGGING
            # ------------------------------

            status.info("🔤 Performing POS Tagging...")

            pos = POSTagger()

            pos_df = pos.extract_pos(doc)

            pos.save_csv(pos_df)

            progress.progress(30)

            # ------------------------------
            # NAMED ENTITY RECOGNITION
            # ------------------------------

            status.info("🏷 Extracting Named Entities...")

            ner = NamedEntityRecognizer()

            entity_df = ner.extract_entities(doc)

            ner.save_csv(entity_df)

            progress.progress(45)

            # ------------------------------
            # RELATION EXTRACTION
            # ------------------------------

            status.info("🔗 Extracting Relations...")

            relation = RelationExtractor()

            relation_df = relation.extract_relations(doc)

            relation.save_csv(relation_df)

            progress.progress(60)

            # ------------------------------
            # EVENT EXTRACTION
            # ------------------------------

            status.info("📅 Detecting Events...")

            events = EventExtractor()

            event_df = events.extract_events(doc)

            events.save_csv(event_df)

            progress.progress(75)

            # ------------------------------
            # TIMELINE
            # ------------------------------

            status.info("🕒 Creating Timeline...")

            timeline = TemporalOrdering()

            timeline_df = timeline.create_timeline(
                event_df
            )

            timeline.save_csv(timeline_df)

            progress.progress(90)

            # ------------------------------
            # VISUALIZATION
            # ------------------------------

            status.info("📊 Generating Graphs...")

            visual = Visualizer()

            visual.pos_distribution(pos_df)

            visual.entity_distribution(entity_df)

            visual.top_entities(entity_df)

            visual.timeline_graph(timeline_df)

            progress.progress(100)

            status.success("✅ Analysis Completed Successfully!")

            st.divider()

            st.header("📈 Analysis Dashboard")

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "POS Tags",
                len(pos_df)
            )

            c2.metric(
                "Entities",
                len(entity_df)
            )

            c3.metric(
                "Relations",
                len(relation_df)
            )

            c4.metric(
                "Events",
                len(event_df)
            )
            st.markdown("---")

            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
                "🔤 POS Tags",
                "🏷 Named Entities",
                "🔗 Relations",
                "📅 Events",
                "🕒 Timeline",
                "📊 Visualizations"
            ])

            # ============================================================
            # POS TAGS
            # ============================================================

            with tab1:

                st.subheader("Part of Speech Tags")

                search_word = st.text_input(
                    "Search Word",
                    key="pos_search"
                )

                if search_word:
                    filtered = pos_df[
                        pos_df["Word"].str.contains(
                            search_word,
                            case=False,
                            na=False
                        )
                    ]
                    st.dataframe(filtered, use_container_width=True)
                else:
                    st.dataframe(pos_df, use_container_width=True)

                st.download_button(
                    "⬇ Download POS CSV",
                    pos_df.to_csv(index=False),
                    "pos_tags.csv",
                    "text/csv"
                )

            # ============================================================
            # NER
            # ============================================================

            with tab2:

                st.subheader("Named Entities")

                entity_type = st.selectbox(
                    "Filter Entity Type",
                    ["All"] + sorted(entity_df["Label"].unique().tolist())
                )

                if entity_type == "All":
                    display_df = entity_df
                else:
                    display_df = entity_df[
                        entity_df["Label"] == entity_type
                    ]

                st.dataframe(
                    display_df,
                    use_container_width=True
                )

                st.download_button(
                    "⬇ Download Entities CSV",
                    entity_df.to_csv(index=False),
                    "entities.csv",
                    "text/csv"
                )

            # ============================================================
            # RELATIONS
            # ============================================================

            with tab3:

                st.subheader("Relation Extraction")

                st.dataframe(
                    relation_df,
                    use_container_width=True
                )

                st.download_button(
                    "⬇ Download Relations CSV",
                    relation_df.to_csv(index=False),
                    "relations.csv",
                    "text/csv"
                )

            # ============================================================
            # EVENTS
            # ============================================================

            with tab4:

                st.subheader("Detected Events")

                st.dataframe(
                    event_df,
                    use_container_width=True
                )

                st.download_button(
                    "⬇ Download Events CSV",
                    event_df.to_csv(index=False),
                    "events.csv",
                    "text/csv"
                )

            # ============================================================
            # TIMELINE
            # ============================================================

            with tab5:

                st.subheader("Timeline")

                st.dataframe(
                    timeline_df,
                    use_container_width=True
                )

                st.download_button(
                    "⬇ Download Timeline CSV",
                    timeline_df.to_csv(index=False),
                    "timeline.csv",
                    "text/csv"
                )

            # ============================================================
            # VISUALIZATIONS
            # ============================================================

            with tab6:

                st.subheader("Analysis Graphs")

                if os.path.exists("visuals/pos_distribution.png"):
                    st.image(
                        "visuals/pos_distribution.png",
                        caption="POS Distribution"
                    )

                if os.path.exists("visuals/entity_distribution.png"):
                    st.image(
                        "visuals/entity_distribution.png",
                        caption="Entity Distribution"
                    )

                if os.path.exists("visuals/top_entities.png"):
                    st.image(
                        "visuals/top_entities.png",
                        caption="Top Entities"
                    )

                if os.path.exists("visuals/timeline.png"):
                    st.image(
                        "visuals/timeline.png",
                        caption="Timeline"
                    )# ============================================================
# INTERACTIVE DASHBOARD
# ============================================================

            st.markdown("---")

            st.header("📊 Interactive Dashboard")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Entity Distribution")

                entity_chart = (
                    entity_df["Label"]
                    .value_counts()
                    .reset_index()
                )

                entity_chart.columns = ["Entity Type", "Count"]

                fig = px.bar(
                    entity_chart,
                    x="Entity Type",
                    y="Count",
                    color="Entity Type",
                    title="Named Entity Distribution"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            with col2:

                st.subheader("POS Distribution")

                pos_chart = (
                    pos_df["POS"]
                    .value_counts()
                    .reset_index()
                )

                pos_chart.columns = ["POS", "Count"]

                fig2 = px.pie(
                    pos_chart,
                    names="POS",
                    values="Count",
                    title="POS Distribution"
                )

                st.plotly_chart(
                    fig2,
                    use_container_width=True
                )

# ============================================================
# TOP ENTITIES
# ============================================================

            st.subheader("🏆 Top 10 Named Entities")

            top_entities = (
                entity_df["Entity"]
                .value_counts()
                .head(10)
                .reset_index()
            )

            top_entities.columns = ["Entity", "Frequency"]

            fig3 = px.bar(
                top_entities,
                x="Entity",
                y="Frequency",
                color="Frequency",
                title="Top Named Entities"
            )

            st.plotly_chart(
                fig3,
                use_container_width=True
            )

# ============================================================
# DOWNLOAD SECTION
# ============================================================

            st.markdown("---")

            st.header("⬇ Download Results")

            c1, c2, c3 = st.columns(3)

            with c1:

                with open(
                    "outputs/entities.csv",
                    "rb"
                ) as f:

                    st.download_button(
                        "Download Entities",
                        f,
                        "entities.csv"
                    )

            with c2:

                with open(
                    "outputs/relations.csv",
                    "rb"
                ) as f:

                    st.download_button(
                        "Download Relations",
                        f,
                        "relations.csv"
                    )

            with c3:

                with open(
                    "outputs/events.csv",
                    "rb"
                ) as f:

                    st.download_button(
                        "Download Events",
                        f,
                        "events.csv"
                    )