# 1.1. Acesso ao site: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
# 1.2. Download dos Anexos I e II em formato PDF: 
# 1.3. Compactação de todos os anexos em um único arquivo (formatos ZIP, RAR, etc.). 

from Conversao.conversao import Compactar
import requests
from bs4 import BeautifulSoup

import os



class PDF(Compactar):
    def __init__(self, url):
        super().__init__()
        self.__url = url
        self.__pdf_List = []
        self.__response = requests.get(self.__url)
        self.__soup = BeautifulSoup(self.__response.text, "html.parser")
        self.__get_AllLinks = self.__soup.find_all("a", class_="internal-link")
        
        
        
    # EXTRAIR PDF DA PAGINA HTML
    def ExtrairPDF(self):
        for link in self.__get_AllLinks:
            dataTip = link.get("data-tippreview-enabled")
            href = link.get("href")

            if 'pdf' in link["href"] and dataTip == "true" :
                self.__pdf_List.append(href)


    # CRIAR REPOSITORIO CASO NAO EXISTA
    # INSTALA PDF E ADICIONA NA PASTA data/pdf
    def BaixarPDF(self):
        try:
            os.makedirs(self._pdf_dir, exist_ok=True)

            for i, pdf_url in enumerate(self.__pdf_List): 
                pdf_response = requests.get(pdf_url, stream=True)
                pdf_path = os.path.join(self._pdf_dir, f"Anexo{i+1}.pdf")

                with open(pdf_path, "wb") as pdf_file:
                    for chunk in pdf_response.iter_content(chunk_size=8192):  
                        if chunk:  
                            pdf_file.write(chunk)
                    print(f"PDF {i+1} BAIXADO")  
        except Exception as e:
            print("Error: ", e)
        
    
