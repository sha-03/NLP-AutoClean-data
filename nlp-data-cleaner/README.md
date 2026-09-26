# NLP Data Cleaner

A small command-line utility for cleaning text in CSV datasets. It removes HTML tags and URLs, decodes HTML entities, and normalizes whitespace. Optional flags lowercase text and remove a built-in list of English stop words.

## Requirements

Python 3.10 or newer. No third-party packages are required.

## Run

From this project directory:

```bash
python app.py data/raw/input.csv data/cleaned/output.csv --text-column text --lowercase
```

Add `--remove-stopwords` to remove common English stop words. Change `text` to the name of the text column in your CSV. The source file is left unchanged; the output directory is created automatically.

For example, a CSV with a header such as `id,text` can be placed in `data/raw/`, then the output will be written under `data/cleaned/`.
