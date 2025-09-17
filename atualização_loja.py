import time
import pandas as pd
from sqlalchemy import create_engine
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DB_USER = "root"
DB_PASS = "vAZILE666"
DB_HOST = "localhost"
DB_NAME = "loja"

engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

def processador_excel():
    try:
        df = pd.read_excel("Produtos_Planilha1_.xlsx")
        df.to_sql("preco", con=engine, if_exists="replace", index=False)
        print("Banco atualizado com sucesso!")
    except Exception as e:
        print("Erro ao atualizar:", e)

    class Monitoramento(FileSystemEventHandler):
        