import time
import pandas as pd
from sqlalchemy import create_engine
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DB_USER = "root"
DB_PASS = "vAZILE666"
DB_HOST = "localhost"
DB_NAME = "loja"

# Conexão com o banco
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

# Função para processar Excel e atualizar o banco
def processador_excel():
    try:
        df = pd.read_excel("Produtos_Planilha1_.xlsx")
        df.to_sql("preco", con=engine, if_exists="replace", index=False)
        print("Banco atualizado com sucesso!")
    except Exception as e:
        print("Erro ao atualizar:", e)

# Classe de monitoramento
class Monitoramento(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("Produtos_Planilha1_.xlsx"):
            print("Arquivo modificado e atualizado no banco")
            processador_excel()

if __name__ == "__main__":
    caminho = "."  # Diretório atual
    observer = Observer()
    observer.schedule(Monitoramento(), path=caminho, recursive=False)
    observer.start()

    print("Monitoramento iniciado. Pressione CTRL+C para parar.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()