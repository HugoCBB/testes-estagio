# 1.1. Acesso ao site: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
# 1.2. Download dos Anexos I e II em formato PDF: 
# 1.3. Compactação de todos os anexos em um único arquivo (formatos ZIP, RAR, etc.). 

import requests
from bs4 import BeautifulSoup
import os



class PDF:
    def __init__(self, url):
        self.url = url
        self.pdf_List = []
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.get_AllLinks = self.soup.find_all("a", class_="internal-link")

        
    
    def ExtrairPDF(self):
        for link in self.get_AllLinks:
            dataTip = link.get("data-tippreview-enabled")
            href = link.get("href")

            if 'pdf' in link["href"] and dataTip == "true" :
                self.pdf_List.append(href)

    def BaixarPDF(self):
        try:
            # CRIAR REPOSITORIO CASO NAO EXISTA
            pdf_dir = os.path.join(os.path.dirname(__file__), "../data/pdf")
            os.makedirs(pdf_dir, exist_ok=True)

            for i, pdf_url in enumerate(self.pdf_List):
                pdf_response = requests.get(pdf_url, stream=True)
                pdf_path = os.path.join(pdf_dir, f"Anexo{i+1}.pdf")

                with open(pdf_path, "wb") as pdf_file:
                    for chunk in pdf_response.iter_content(chunk_size=8192):  
                        if chunk:  
                            pdf_file.write(chunk)
                    print(f"PDF {i+1} BAIXADO: {pdf_path}")  
        except Exception as e:
            print("Error: ", e)
        



if __name__ == "__main__":
    client = PDF("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
    client.ExtrairPDF()
    client.BaixarPDF()
