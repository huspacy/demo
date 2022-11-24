---
title: HuSpaCy Demo
emoji: 🚀
colorFrom: indigo
colorTo: gray
sdk: streamlit
sdk_version: 1.10.0
app_file: app.py
pinned: true
---

# 🚀 HuSpaCy Demo

This repository contains an app demonstrating the capabilities of [HuSpaCy](https://github.com/spacy-hu/spacy-hungarian-models). The demo is available at [Hugging Face Spaces](https://huggingface.co/spaces/huspacy/demo)

## Development

To start the demo: `poetry run python app.py`

If you upgrade dependencies via poetry don't forget to update `requirements.txt` with `poetry export --without-hashes > requirements.txt`