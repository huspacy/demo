import spacy_streamlit

models = ["hu_core_news_lg"]
default_text = "Ezután Király Márton, a beruházó cég projektvezetője mesélte el, hogy a területet 2006-ban vásárolta meg az önkormányzattól az első tulajdonos."
spacy_streamlit.visualize(models, default_text)
