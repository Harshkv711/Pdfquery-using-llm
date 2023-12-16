from langchain.vectorstores.cassandra import Cassandra 
from langchain.indexes.vectorstore import VectorStoreIndexWrapper 
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings 
import cassio 
from PyPDF2 import PdfReader 
from typing_extensions import Concatenate
from langchain.text_splitter import CharacterTextSplitter 

ASTRA_DB_APPLICATION_TOKEN = "Add your astra token here"
ASTRA_DB_ID = "Add your astra db id here"
OpenAI_API_KEY = "add your openAI api key here"

def read_pdf(file_path):
    pdfreader = PdfReader(file_path)
    raw_text = ''
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text

def initialize_astra_db():
    cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

def get_user_input():
    file_path = input("Enter the path of the PDF file: ").strip()
    return file_path

def process_pdf_and_queries(raw_text, astra_vector_store, llm):
    texts = text_splitter.split_text(raw_text)
    astra_vector_store.add_texts(texts[:50])
    print("Inserted %i chunks of text." % len(texts[:50]))
    astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

    first_question = True
    while True:
        if first_question:
            query_text = input("\nEnter your question (or type 'quit' to exit): ").strip()
        else:
            query_text = input("\nWhat's your next question (or type 'quit' to exit): ").strip()

        if query_text.lower() == "quit":
            break

        if query_text == "":
            continue

        first_question = False

        print("\nQUESTION: \"%s\"" % query_text)
        answer = astra_vector_index.query(query_text, llm=llm).strip()
        print("ANSWER: \"%s\"\n" % answer)

        print("FIRST DOCUMENTS BY RELEVANCE:")
        for doc, score in astra_vector_store.similarity_search_with_score(query_text, k=4):
            print("    [%0.4f] \"%s ...\"" % (score, doc.page_content[:84]))

if __name__ == "__main__":
    initialize_astra_db()
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=800, chunk_overlap=200, length_function=len)
    embedding = OpenAIEmbeddings(openai_api_key=OpenAI_API_KEY)
    astra_vector_store = Cassandra(embedding=embedding, table_name="qa_mini_demo", session=None, keyspace=None)
    llm = OpenAI(openai_api_key=OpenAI_API_KEY)

    while True:
        file_path = get_user_input()

        try:
            pdf_text = read_pdf(file_path)
            process_pdf_and_queries(pdf_text, astra_vector_store, llm)
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")
        except Exception as e:
            print("An error occurred:", e)
