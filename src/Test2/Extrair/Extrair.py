import camelot
import pandas as pd
import os
from Conversao.conversao import Compactar

class ExtrairDados(Compactar):
    def __init__(self):
        super().__init__()
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/pdf/Anexo1.pdf"))
        self.tables = camelot.read_pdf(self.base_dir, pages="3-end", flavor="stream")


    def SalvarCSV(self):
        if self.tables.n > 0:
            os.makedirs(self._csv_dir, exist_ok=True)
            df_final = pd.DataFrame()


            for _, table in enumerate(self.tables):
                
                df = table.df.apply(lambda x: x.str.replace("\n", " ").str.strip()) 

                df_final = df_final.dropna(how="all", axis=1)
                df_final = df_final.dropna(how="all", axis=0)
                
                df_final = pd.concat([df_final, df], ignore_index=True)
            output_path = os.path.join(self._csv_dir, "Tabelas.csv")
            df_final.to_csv(output_path, index=False)
            
        else:
            print("Nenhuma tabela encontrada")
        
            

if __name__ == "__main__":
    client = ExtrairDados()
    # client.SalvarCSV()
    client.CompactarZipCSV()