# ImgToSummary

ImgToSummary is a Python project that extracts text from images, preprocesses the text, and summarizes the text using OpenAI's GPT model. The project uses Optical Character Recognition (OCR) to extract text from images, natural language processing (NLP) techniques to preprocess the text, and a large language model (LLM) to summarize the text.

## Features

- Extracts text from images using the UnstructuredImageLoader class from the langchain_community library.
- Preprocesses the text using tokenization, lowercasing, punctuation removal, stop word removal, stemming, and lemmatization.
- Summarizes the text using OpenAI's GPT model.

ImgToSummary/
│
├── orc/
│   ├── __init__.py
│   ├── image_loader.py
│
├── llm/
│   ├── __init__.py
│   ├── openai_model.py
│
├── preprocessing/
│   ├── __init__.py
│   ├── text_preprocessing.py
│
├── main.py
├── .env

