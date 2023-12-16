PDF Text Extraction and Interactive Querying

This Python script enables users to extract text from a PDF file of their choice, store the text data in AstraDB using Cassandra, and perform interactive querying to retrieve relevant information based on user-input questions.

Features

- Extracts text content from a PDF file.
- Stores the extracted text in AstraDB with Cassandra.
- Utilizes OpenAI's language model for interactive querying based on user input.
- Allows users to input questions and retrieves relevant answers from the stored text data.

Requirements

- Python 3.x
- AstraDB (Cassandra)

 Setup and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pdf-text-extraction.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up AstraDB and Obtain Keys:

   - Obtain your AstraDB Application Token and Database ID.
   - Update the `ASTRA_DB_APPLICATION_TOKEN` and `ASTRA_DB_ID` variables in the script with your credentials.

4. Set up OpenAI API:

   - Obtain your OpenAI API Key.
   - Update the `OpenAI_API_KEY` variable in the script with your API key.

5. Run the script:

   ```bash
   python pdf_text_extraction.py
   ```

6. Follow the prompts:

   - Enter the path of the PDF file you want to process.
   - Input your questions when prompted.
   - Receive answers based on the stored text data and OpenAI's language model.

Usage Example

```bash
Enter the path of the PDF file: /path/to/your/pdf/file.pdf

Enter your question (or type 'quit' to exit): What is the capital of France?
```

Notes

- Ensure the PDF file path provided is valid.
- Queries are case-insensitive but try to be as specific as possible for accurate results.
- Type 'quit' at any time to exit the script.

