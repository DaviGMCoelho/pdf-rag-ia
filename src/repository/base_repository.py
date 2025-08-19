from data.database.database import ChromaDatabase
from langchain_chroma.vectorstores import Chroma

class BaseRepository:
    def __init__(self, database: ChromaDatabase):
        self.database = database

    def _insert_data(self, documents):
        self.database.insert_data(documents)

    def _search_database(self, content, embedding):
        database = Chroma(persist_directory=self.database.db_path, embedding_function=embedding)
        results = database.similarity_search_with_relevance_scores(content, k=5)
        return results
