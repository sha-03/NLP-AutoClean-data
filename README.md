# 🧹 NLP Data Cleaner

A simple and lightweight **NLP-based CSV data cleaning tool** built with Python.

This project helps clean messy text data inside CSV files automatically. It removes unwanted elements such as HTML tags, URLs, extra spaces, and HTML entities, making the dataset easier to use for NLP and machine learning tasks.

---

## ✨ Features

The NLP Data Cleaner can:

- 🧹 Remove HTML tags
- 🔗 Remove URLs
- 🔤 Decode HTML entities
- 🧼 Remove unnecessary spaces
- 🔡 Convert text to lowercase
- 🚫 Remove common English stop words
- 📂 Read CSV files
- 💾 Save the cleaned data into a new CSV file
- 🔒 Keep the original dataset unchanged

---

## 📁 Project Structure

```text
nlp-data-cleaner/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── cleaner.py
│   ├── nlp_processor.py
│   ├── utils.py
│   └── validator.py
│
└── data/
    ├── raw/
    │   └── input.csv
    │
    └── cleaned/
        └── output.csv
