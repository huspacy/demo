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

# Citation

If you use HuSpaCy or any of its models, please cite it as:

[![arxiv](http://img.shields.io/badge/cs.CL-arXiv%3A2308.12635-B31B1B.svg)](https://arxiv.org/abs/2308.12635)

```bibtex
@InProceedings{HuSpaCy:2023,
    author= {"Orosz, Gy{\"o}rgy and Szab{\'o}, Gerg{\H{o}} and Berkecz, P{\'e}ter and Sz{\'a}nt{\'o}, Zsolt and Farkas, Rich{\'a}rd"},
    editor= {"Ek{\v{s}}tein, Kamil and P{\'a}rtl, Franti{\v{s}}ek and Konop{\'i}k, Miloslav"},
    title = {{"Advancing Hungarian Text Processing with HuSpaCy: Efficient and Accurate NLP Pipelines"}},
    booktitle = {{"Text, Speech, and Dialogue"}},
    year = "2023",
    publisher = {{"Springer Nature Switzerland"}},
    address = {{"Cham"}},
    pages = "58--69",
    isbn = "978-3-031-40498-6"
}
```

[![arxiv](http://img.shields.io/badge/cs.CL-arXiv%3A2201.01956-B31B1B.svg)](https://arxiv.org/abs/2201.01956)

```bibtex
@InProceedings{HuSpaCy:2021,
  title = {{HuSpaCy: an industrial-strength Hungarian natural language processing toolkit}},
  booktitle = {{XVIII. Magyar Sz{\'a}m{\'\i}t{\'o}g{\'e}pes Nyelv{\'e}szeti Konferencia}},
  author = {Orosz, Gy{\"o}rgy and Sz{\' a}nt{\' o}, Zsolt and Berkecz, P{\' e}ter and Szab{\' o}, Gerg{\H o} and Farkas, Rich{\' a}rd},
  location = {{Szeged}},
  pages = "59--73",
  year = {2022},
}
```


## Development

To start the demo: `poetry run python app.py`

If you upgrade dependencies via poetry don't forget to update `requirements.txt` with `poetry export --without-hashes > requirements.txt`
