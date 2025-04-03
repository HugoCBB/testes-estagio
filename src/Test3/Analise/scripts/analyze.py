
# from queries import queries

# class Analyze:
#     def __init__(self):
#         super().__init__()
    
#     def IniciarQuery(self):
#         pass

import os
import pandas as pd
from database import Database
from queries import queries

# Rodar queries e salvar resultados
p1 = Database()

# Diretório para salvar os resultados
processed_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../processed"))
os.makedirs(processed_dir, exist_ok=True)

for name, query in queries.items():
    df = pd.read_sql(query, p1.engine)
    output_path = os.path.join(processed_dir, f"{name}.csv")
    df.to_csv(output_path, index=False)
    print(f"Resultados de {name} salvos com sucesso em {output_path}!")