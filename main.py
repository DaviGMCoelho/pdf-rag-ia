import os
from langchain_ollama import OllamaEmbeddings
from data.database.database import ChromaDatabase
from src.repository.language_repository import LanguageRepository
from src.repository.file_repository import FileRepository
from src.validation.validation import Validation
from src.service.language_service import LanguageService
from src.service.file_service import FileService
from src.controller.language_controller import LanguageController
from src.controller.file_controller import FileController
from src.view.main_window import MainWindow




class Main():
    def __init__(self):
        self.model = 'mistral:latest'
        self.model_embedding = 'nomic-embed-text-v1.5-multimodal'
        self.language_validation = Validation()
        self.ollama_embedding = OllamaEmbeddings(model=self.model_embedding)

        self.database = ChromaDatabase(self.ollama_embedding)

        self.language_repository = LanguageRepository(self.database)
        self.file_repository = FileRepository(self.database)

        self.language_service = LanguageService(self.model, self.ollama_embedding, self.language_repository, self.language_validation)
        self.file_service = FileService(self.file_repository)

        self.language_controller = LanguageController(self.language_service)
        self.file_controller = FileController(self.file_service)

        self.main_window = MainWindow(self.file_controller, self.language_controller)

    def run(self):
        self.main_window.window()


program = Main()
program.run()
