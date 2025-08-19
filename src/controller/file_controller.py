from src.service.file_service import FileService

class FileController():
    def __init__(self, file_service: FileService):
        self.file_service = file_service

    def upload_pdfs(self, folder_path):
        path = fr'{folder_path}'
        self.file_service.load_pdf(path)
