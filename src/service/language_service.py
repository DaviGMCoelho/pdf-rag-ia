from src.validation.validation import Validation
from src.repository.language_repository import LanguageRepository

from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate

class LanguageService:
    def __init__(self, model: str, embedding: object, repository: LanguageRepository, validation: Validation):
        self.model = model
        self.embedding = embedding
        self.repository = repository
        self.validation = validation

        self.prompt_template = '''
        Answer the user question: 
        {question}
        Using this data: {database}'''

    def generate_answer(self, question:str):
        chunks = self.repository._search_database(question, self.embedding)
        if chunks is None or len(chunks) == 0:
            return 'Não consegui encontrar uma informação relevante'
        
        database = self.validation.exists(chunks)
        
        prompt = ChatPromptTemplate.from_template(self.prompt_template)
        prompt = prompt.invoke({"question": question, "database": database})

        language_model = ChatOllama(model=self.model)
        response_text = language_model.invoke(prompt).content
        return response_text
