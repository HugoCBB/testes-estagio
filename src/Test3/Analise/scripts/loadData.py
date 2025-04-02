from database import Database
import pandas as pd
import os

# MIGRA OS DADOS DENTRO DO CSV PARA O BANCO DE DADOS
class LoadData:
    def __init__(self):
        super().__init__()
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
        self.csv_path = os.path.join(self.base_dir, "data/csv/Arquivo8.csv")
        self.db = Database()
        self.engine = self.db.engine

    def ImportData(self):
        self.df = pd.read_csv(self.csv_path, delimiter=";")
        self.df.to_sql("despesas_saude", self.engine, if_exists="replace", index=False)
        
        print("Dados importados")

p1 = LoadData()
p1.ImportData()