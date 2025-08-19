from src.repository.file_repository import FileRepository

from langchain_community.document_loaders import PyPDFDirectoryLoader # Read pdf archives


class FileService():
    def __init__(self, repository: FileRepository):
        self.repository = repository

    def load_pdf(self, folder_path):
        pdf_loader = PyPDFDirectoryLoader(folder_path, glob='*.pdf')
        documents = pdf_loader.load()
        self.repository.load_pdf_documents(documents)
