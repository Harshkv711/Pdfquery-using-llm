from flask import Flask, render_template, request
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from cassandra.cluster import Cluster

app = Flask(__name__)

# Cassandra connection details
cluster = Cluster(['10.16.89.5'])  # Replace with your Cassandra node IP
session = cluster.connect('keyspace')  # Replace 'your_keyspace' with your actual keyspace name

# Check if the connection is successful
if session:
    print("Connected to Cassandra cluster")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    global session  # Define session as a global variable

    pdfreader = PdfReader('kotler.pdf')
    raw_text = ''
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content

    llm = OpenAI(openai_api_key="YOUR_OPENAI_API_KEY")  # Replace with your OpenAI API key
    embedding = OpenAIEmbeddings(openai_api_key="YOUR_OPENAI_API_KEY")  # Replace with your OpenAI API key

    # Create a Cassandra vector store
    astra_vector_store = Cassandra(
        embedding=embedding,
        table_name="qa_mini_demo",
        session=session,  # Use the session created earlier
        keyspace="keyspace",  # Replace 'your_keyspace' with your actual keyspace name
    )

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
    )

    texts = text_splitter.split_text(raw_text)

    astra_vector_store.add_texts(texts[:50])
    print("Inserted %i headlines." % len(texts[:50]))
    astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

    query_text = request.form['query_text'].strip()

    print("\nQUESTION: \"%s\"" % query_text)
    answer = astra_vector_index.query(query_text, llm=llm).strip()
    print("ANSWER: \"%s\"\n" % answer)

    return answer

if __name__ == '__main__':
    app.run(debug=True)
