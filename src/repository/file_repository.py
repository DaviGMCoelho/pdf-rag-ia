
from src.repository.base_repository import BaseRepository

class FileRepository (BaseRepository):

    def load_pdf_documents(self, documents):
        self._insert_data(documents)
