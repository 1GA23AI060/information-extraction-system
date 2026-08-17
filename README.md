#  Information Extraction System

A Python-based **Information Extraction System** that processes news articles and extracts structured information such as Part-of-Speech (POS) tags, named entities, relationships, and events. The extracted information is presented through an interactive Streamlit dashboard.

##  Features

-  News article preprocessing and text cleaning
-  Part-of-Speech (POS) tagging
-  Named Entity Recognition (NER)
-  Relation extraction
-  Event extraction
-  Event and temporal analysis
-  Interactive data visualizations
-  Entity and POS distribution analysis
-  Export extracted results as CSV files
-  Interactive Streamlit dashboard

##  Technologies Used

- **Python 3.11+** – Backend programming
- **spaCy** – NLP processing, POS tagging and NER
- **Pandas** – Dataset and result handling
- **NumPy** – Numerical processing
- **Matplotlib / Plotly** – Data visualization
- **Streamlit** – Interactive frontend
- **CSV** – Dataset and output storage

##  Project Structure


Information_Extraction_System/
│
├── app.py
├── main.py
├── README.md
├── requirements.txt
├── true.csv
│
├── dataset/
│   └── news articles / input data
│
├── outputs/
│   ├── entities.csv
│   ├── relations.csv
│   ├── events.csv
│   └── other generated results
│
├── src/
│   ├── preprocessing.py
│   ├── pos_tagging.py
│   ├── entities.py
│   ├── relations.py
│   ├── events.py
│   └── visualization.py
│
├── visuals/
│   └── generated charts
│
└── venv/
    └── virtual environment
````

##  Setup Instructions

### 1. Clone or open the project

Open the project folder in VS Code.

```bash
cd Information_Extraction_System
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

For macOS/Linux:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If spaCy is used, install the English language model:

```bash
python -m spacy download en_core_web_sm
```

##  Running the Backend

The backend performs the main information extraction and analysis.

Run:

```bash
python main.py
```

The backend processes the dataset and generates the extracted results inside the `outputs/` folder.

Typical outputs include:

```text
outputs/
├── entities.csv
├── relations.csv
├── events.csv
└── pos.csv
```

##  Running the Frontend

The frontend is implemented using **Streamlit** and provides an interactive dashboard for viewing the extracted information.

Run:

```bash
streamlit run app.py
```

or:

```bash
python -m streamlit run app.py
```

After starting Streamlit, open the URL displayed in the terminal, usually:

```text
http://localhost:8501
```

##  System Workflow

```text
News Dataset
     ↓
Data Loading
     ↓
Text Preprocessing
     ↓
POS Tagging
     ↓
Named Entity Recognition
     ↓
Relation & Event Extraction
     ↓
Result Generation
     ↓
Visualization & Analysis
     ↓
Streamlit Dashboard
```

##  Dashboard

The Streamlit dashboard allows users to:

* View the total number of processed records
* Explore POS tags
* View extracted named entities
* Examine relationships between entities
* View extracted events
* Analyze entity and POS distributions
* View top named entities
* Download extracted results as CSV files

##  Dataset

The system uses a news-article dataset containing textual information that is processed by the NLP pipeline.

The dataset is stored in the project dataset/input directory and is processed before information extraction.

##  Output

The system generates structured outputs such as:

* POS tagging results
* Named entity results
* Relation extraction results
* Event extraction results
* Statistical summaries
* Visualization charts

The generated files are stored in:

```text
outputs/
```

##  NLP Pipeline

### POS Tagging

spaCy identifies the grammatical category of each word, such as noun, verb, adjective, and proper noun.

### Named Entity Recognition

The system identifies entities such as:

* PERSON
* ORGANIZATION
* DATE
* LOCATION
* EVENT
* PRODUCT
* MONEY
* TIME

### Relation Extraction

Relationships between identified entities are extracted from the processed text.

### Event Extraction

Important events and associated temporal information are identified from the news articles.

##  Troubleshooting

### `ModuleNotFoundError`

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### `No module named spacy`

```bash
pip install spacy
```

### `No module named streamlit`

```bash
pip install streamlit
```

### spaCy model not found

Run:

```bash
python -m spacy download en_core_web_sm
```

### Streamlit does not start

Make sure the virtual environment is activated and run:

```bash
python -m streamlit run app.py
```

##  Project Objective

The objective of this project is to build an end-to-end **Information Extraction System** that converts unstructured news text into structured linguistic and semantic information using Natural Language Processing techniques.

##  License

This project is developed for educational purposes as part of the **Advanced Natural Language Processing (AML23702)** laboratory.

---

````

### One important correction for your project

From your screenshot, your actual frontend is clearly **Streamlit**, and your main files are `app.py` and `main.py`. So the two commands you should document are:

**Backend:**
```bash
python main.py
````

**Frontend:**

```bash
python -m streamlit run app.py
```

