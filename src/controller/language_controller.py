from src.service.language_service import LanguageService

class LanguageController:
    def __init__(self, language_service: LanguageService):
        self.service = language_service

    def asking(self, question):
        answer = self.service.generate_answer(question)
        return answer