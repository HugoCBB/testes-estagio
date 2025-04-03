from database import Database
import pandas as pd
import os

# MIGRA OS DADOS DENTRO DO CSV PARA O BANCO DE DADOS
class LoadData:
    def __init__(self):
        self.base_dir = os.path.abspath(os.path.dirname(__file__)) 
        self.csv_path = os.path.abspath(os.path.join(self.base_dir, "../../../../data/csv/"))
        self.db = Database()
        self.engine = self.db.engine

        os.makedirs(self.csv_path, exist_ok=True)

    """
    Importa todos os arquivos CSV para o banco de dados.
    """
    def ImportData(self):
        if not os.path.exists(self.csv_path):
            print(f"Diretório não encontrado: {self.csv_path}")
            return
        
        arquivos_csv = [f for f in os.listdir(self.csv_path) if f.endswith(".csv")]

        if not arquivos_csv:
            print("Nenhum arquivo CSV encontrado para importar.")
            return
        
        for arquivo in arquivos_csv:
            caminho_completo = os.path.join(self.csv_path, arquivo)  
        

            try:
                if os.path.exists(caminho_completo): 
                    df = pd.read_csv(caminho_completo, delimiter=";")  

                    df.columns = df.columns.str.lower()

                    
                    df.to_sql("despesas_saude", self.engine, if_exists="append", index=False)
                    print(f"Dados de {arquivo} importados com sucesso.")
                else:
                    print(f"Arquivo não encontrado: {caminho_completo}")

            except Exception as e:
                print(f" Erro ao importar: {e}")

p1 = LoadData()
p1.ImportData()