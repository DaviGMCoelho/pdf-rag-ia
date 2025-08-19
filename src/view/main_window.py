import os

from src.controller.file_controller import FileController
from src.controller.language_controller import LanguageController

class MainWindow():
    def __init__(self, file_controller: FileController, language_controller: LanguageController):
         self.file_controller = file_controller
         self.language_controller = language_controller

    def clean_terminal(self):
        """Limpa o terminal."""
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux, macOS
            os.system('clear')

    def window(self):
        while True:
            self.clean_terminal()
            print('--------------------- Menu de Opções ---------------------')
            print('- 1. Adicionar novos documentos (Pasta)')
            print('- 2. Realizar perguntas ao modelo')
            print('- 3. Respostas para perguntas frequentes - FAQ.')
            print('- 0. Fechar programa.')
            print('----------------------------------------------------------')
            choice = input('- Digite a opção desejada: ')
            print('----------------------------------------------------------')

            match choice:
                case "1":
                    self.clean_terminal()
                    print('----------------------------------------------------------')
                    print('---              Adicionando novos dados!              ---')
                    print('----------------------------------------------------------')
                    try:
                        print('- Lendo arquivos em "documents"... ')
                        self.file_controller.upload_pdfs('documents')
                        print('- Leitura realizada!')
                        print('----------------------------------------------------------')
                        input('Aperte enter para continuar... ')
                    except Exception as error:
                        print(f'- Um erro ocorreu: {error}')
                        print('----------------------------------------------------------')
                        input('Aperte enter para continuar... ')

                case "2":
                    self.clean_terminal()
                    print('----------------------------------------------------------')
                    print('---               Falando com o sistema!               ---')
                    print('----------------------------------------------------------')
                    while True:
                        question = input('Pergunta (0 para sair): ')
                        if question == 0:
                            print('- Saindo...')
                            break
                        answer = self.language_controller.asking(question)
                        print(f'\nResposta: {answer}\n\n')

                case "3":
                    self.clean_terminal()
                    print('----------------------------------------------------------')
                    print('---                        FAQ!                        ---')
                    print('----------------------------------------------------------')
                    print('- Pergunta: Como mudar os modelos padrão?')
                    print('- Entre em "main" e altere o modelo em "self.model".')
                    print('-                 ----------------------')
                    print('- Pergunta: Como adiciono meus arquivos?')
                    print('- Resposta: Adicione todos eles na pasta "documents".')
                    print('-    Os arquivos nessa pasta são lidos automaticamente ao')
                    print('- escolher a opção "Adicionar novos documentos"')
                    print('----------------------------------------------------------')
                    input('Aperte enter para continuar... ')

                case "0":
                    self.clean_terminal()
                    print('----------------------------------------------------------')
                    print('---                      Até mais!                     ---')
                    print('----------------------------------------------------------')
                    input('Aperte enter para continuar... ')
                    break

                case _:
                    self.clean_terminal()
                    print('Essa opção não existe, escolha uma opção válida!')
                    input('Aperte enter para continuar... ')
