import requests

from Conversao.conversao import Compactar

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import zipfile

import os

from time import sleep


class OperadoraDespesa(Compactar):
    def __init__(self):
        super().__init__()
        self.url = ["https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/", 
                    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/",
                    "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"]
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.todosLink = []
        

    
    def ExtrairLinks(self):
        for urls in self.url:
            self.driver.get(urls)
            sleep(2)
            
            link = self.driver.find_elements(By.TAG_NAME, "a")

            for elemento in link:
                href = elemento.get_attribute("href")
                
                if href and href.endswith(".csv"):
                    self.todosLink.append(href)
                
                elif href and href.endswith(".zip"):
                    self.todosLink.append(href)
        self.driver.quit()

    """
    BAIXA ARQUIVO EM .ZIP OU CSV, ALEM DE EXTRAIR OS ARQUIVOS .ZIP EM CSV
    """
    def BaixarArquivos(self):

        for i, link in enumerate(self.todosLink):
            os.makedirs(self._csv_dir, exist_ok=True)
            os.makedirs(self._csv_dir, exist_ok=True)
            try:
                if link.endswith(".zip"):
                    zip_path = os.path.join(self._zip_dir, f"Arquivo{i+1}.zip")
                    response = requests.get(link, stream=True)
                    
                    with open(zip_path, "wb") as arquivo:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                arquivo.write(chunk)
                    print("Arquivo salvo")
                    self.DescompactarZIP(zip_path, i)
                    
                
                if link.endswith(".csv"):
                    csv_path = os.path.join(self._csv_dir, f"Arquivo{i}.csv")
                    response = requests.get(link, stream=True)
                    
                    with open(csv_path, "wb") as arquivo:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                arquivo.write(chunk)
                    print("Arquivo salvo")

            except Exception as e:
                print("error: ", e)

    def DescompactarZIP(self, zip_path, i):
        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(self._csv_dir)
                
                for arquivo in os.listdir(self._csv_dir):
                    if arquivo.endswith(".csv"):
                        caminho_antigo = os.path.join(self._csv_dir, arquivo)
                        caminho_novo = os.path.join(self._csv_dir, f"extraido_{arquivo}")
                        os.rename(caminho_antigo, caminho_novo)
                
                print("Arquivo extraido")
        except Exception as e:
            print("error: ", e)