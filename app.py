import spacy_streamlit
import streamlit as st

st.set_page_config(layout="wide")

models = {"hu_core_news_lg": "hu_core_news_lg"}

default_text = "Jóváhagyták a Netrisk terjeszkedését Ausztriában."

spacy_streamlit.visualize(
    models,
    default_text,
    ["parser", "ner", "tokens", "similarity"],
    show_json_doc=False,
    sidebar_title="🚀 HuSpaCy",
    sidebar_description="Industrial strength Hungarian NLP",
    similarity_texts=("kifli", "zsemle"),
    show_logo=False
)
