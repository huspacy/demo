import spacy_streamlit


models = {"hu_core_news_lg": "hu_core_news_lg"}

default_text = "Újraoltatta magát Szputnyik Light vakcinával a Covid-19 ellen Vlagyimir Putyin orosz elnök."

spacy_streamlit.visualize(
  models,
  default_text,
  ["parser", "ner", "tokens", "similarity"],
  show_json_doc = False,
  sidebar_title = "🚀 HuSpaCy",
  sidebar_description = "Industrial strength Hungarian NLP",
  similarity_texts = ("kifli", "zsemle"),
  show_logo = False
)
