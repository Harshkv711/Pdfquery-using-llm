# Flask-Cassandra-OpenAI-PDF-Query

This repository contains a Flask web application that utilizes Cassandra for data storage, OpenAI for language models, and PyPDF2 for PDF text extraction to perform queries on extracted text.


## Introduction

This Flask web application integrates Cassandra database functionality with OpenAI's language models to facilitate text-based queries on PDF documents. The application extracts text from a provided PDF file and allows users to input queries to retrieve relevant information from the document.

## Features

- PDF text extraction and processing.
- Integration with Cassandra for efficient text storage and retrieval.
- Utilization of OpenAI for language models and embeddings.
- User-friendly web interface for querying text data.

## Technologies Used

- Flask
- Cassandra
- OpenAI
- PyPDF2

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your_username/Flask-Cassandra-OpenAI-PDF-Query.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Cassandra:
   - Ensure Cassandra is installed and running.
   - Update the Cassandra connection details in the code (`cluster` and `session` variables).

4. Obtain OpenAI API Key:
   - Replace `'YOUR_OPENAI_API_KEY'` in the code with your actual OpenAI API key.

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Access the web application by visiting `http://localhost:5000` in your web browser.
3. Upload a PDF file and input queries to retrieve information from the document.

## Contributing

Contributions are welcome! 

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [OpenAI](https://openai.com) for providing language models and embeddings.
- [PyPDF2](https://pythonhosted.org/PyPDF2/) for PDF extraction functionality.

## About

This project was developed by Harsh as a demonstration of integrating Flask, Cassandra, OpenAI, and PDF text extraction for information retrieval purposes.

---

