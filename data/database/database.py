
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma

class ChromaDatabase():
    '''
    Manages the connection to the Chroma database using a singleton pattern.

    Attributes:
        model (str): The current language model used.
        db_path (str): Path to the SQLite database file.
    '''
    
    def __init__(self, embedding: object, db_path=r'data\database'):
        self.db_path = db_path
        self.embedding = embedding
        self.database = Chroma(embedding_function=self.embedding, persist_directory=self.db_path)

    def _create_chunks(self, documents):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 800,
            chunk_overlap = 150,
            length_function=len,
            add_start_index=True
        )
        chunks = splitter.split_documents(documents)
        return chunks

    def _vetorize_chunks(self, chunks):
        self.database.add_documents(chunks)

    def insert_data(self, documents):
        chunks = self._create_chunks(documents)
        self._vetorize_chunks(chunks)
