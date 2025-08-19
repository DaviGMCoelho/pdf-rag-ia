from src.repository.base_repository import BaseRepository
from data.database.database import ChromaDatabase

class LanguageRepository(BaseRepository):
    def __init__(self, database:ChromaDatabase):
        self.database = database