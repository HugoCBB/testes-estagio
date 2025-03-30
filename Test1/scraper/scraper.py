# 1.1. Acesso ao site: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
# 1.2. Download dos Anexos I e II em formato PDF: 
# 1.3. Compactação de todos os anexos em um único arquivo (formatos ZIP, RAR, etc.). 

import requests
from bs4 import BeautifulSoup
import zipfile
import os



class PDF:
    def __init__(self, url):
        self.__url = url
        self.__pdf_List = []
        self.__response = requests.get(self.__url)
        self.__soup = BeautifulSoup(self.__response.text, "html.parser")
        self.__get_AllLinks = self.__soup.find_all("a", class_="internal-link")
        
        self.__pdf_dir = os.path.join(os.path.dirname(__file__), "../data/pdf")
        self.__zip_dir = os.path.join(os.path.dirname(__file__), "../data/zip")
        
    
    def ExtrairPDF(self):
        for link in self.__get_AllLinks:
            dataTip = link.get("data-tippreview-enabled")
            href = link.get("href")

            if 'pdf' in link["href"] and dataTip == "true" :
                self.__pdf_List.append(href)

    def BaixarPDF(self):
        try:
            # CRIAR REPOSITORIO CASO NAO EXISTA
            os.makedirs(self.__pdf_dir, exist_ok=True)

            for i, pdf_url in enumerate(self.__pdf_List): 
                # INSTALA PDF E ADICIONA NA PASTA data/pdf
                pdf_response = requests.get(pdf_url, stream=True)
                pdf_path = os.path.join(self.__pdf_dir, f"Anexo{i+1}.pdf")

                with open(pdf_path, "wb") as pdf_file:
                    for chunk in pdf_response.iter_content(chunk_size=8192):  
                        if chunk:  
                            pdf_file.write(chunk)
                    print(f"PDF {i+1} BAIXADO")  
        except Exception as e:
            print("Error: ", e)
        
    def CompactarZIP(self):
        try:
            os.makedirs(self.__zip_dir, exist_ok=True)
            zip_path = os.path.join(self.__zip_dir, "Anexos.zip")

            # CRIAR UM ARQUIVO .ZIP A PARTIR DOS PDFS E ADICIONA NA PAGINA
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                for root, _, files in os.walk(self.__pdf_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self.__pdf_dir)
                        zip_ref.write(file_path, arcname)

            print(f"ARQUIVO ZIP CRIADO")
        except Exception as e:
            print("error: ",e)
    
