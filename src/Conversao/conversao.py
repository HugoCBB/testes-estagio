import os
import zipfile


class Compactar:
    def __init__(self):
        self._zip_dir = os.path.join(os.path.dirname(__file__), "../../data/zip")
        self._pdf_dir = os.path.join(os.path.dirname(__file__), "../../data/pdf")
        self._csv_dir = os.path.join(os.path.dirname(__file__), "../../data/csv")

    def CompactarZipPDF(self):
        try:
            os.makedirs(self._zip_dir, exist_ok=True)
            zip_path = os.path.join(self._zip_dir, "Anexos.zip")

            # CRIAR UM ARQUIVO .ZIP A PARTIR DOS PDFS E ADICIONA NA PAGINA
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                for root, _, files in os.walk(self._pdf_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self._pdf_dir)
                        zip_ref.write(file_path, arcname)

            print(f"ARQUIVO ZIP CRIADO")
        except Exception as e:
            print("error: ",e)
    
    def CompactarZipCSV(self):
        try:
            os.makedirs(self._zip_dir, exist_ok=True)
            zip_path = os.path.join(self._zip_dir, "Teste_Hugo_Carlos_Barbosa_Brandao.zip")

            # CRIAR UM ARQUIVO .ZIP A PARTIR DOS PDFS E ADICIONA NA PAGINA
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                for root, _, files in os.walk(self._csv_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self._csv_dir)
                        zip_ref.write(file_path, arcname)

            print(f"ARQUIVO ZIP CRIADO")
        except Exception as e:
            print("error: ",e)
