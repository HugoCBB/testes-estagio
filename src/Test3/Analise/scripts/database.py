import yaml
from sqlalchemy import create_engine
import os

class Database:
    def __init__(self):
        self.configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config/config.yaml"))
        
        with open(self.configPath, "r") as file:
            self.config = yaml.safe_load(file)

        self.engine = None
        self.ConnectDatabase()

    def ConnectDatabase(self):
        db_config = self.config["database"]
        
        DATABASE_URL = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"
        engine = create_engine(DATABASE_URL)    
        self.engine = engine
        print("CONEXAO ESTABELECIDA")

