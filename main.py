import os
import shutil
import time

origem = r"C:\pastaorigem"  # Colocar o caminho do explorador de arquivos da pasta de origem dos arquivos
destino = r"\\dom146\pastadestino"  # Colocar o caminho da pasta destino, onde os arquivos serão enviados

def sincronizar_arquivos():
    try:

# Definido um parâmetro: apenas arquivos que contém a palavra
# 'parte' no nome será sincronizada e enviada para o local de destino definido anteriormente, lembrando que isso pode variar de acordo com sua necessidade.
#  Imagine que está transformando um arquivo de 300GB em várias partes
# de 100 mb, a quantidade de arquivos que será gerado e a demora que levará para gerar todos. Enquanto é gerado os arquivos o sistema vai copiando para a pasta 
# destino automaticamente.        
        arquivos_origem = {arquivo for arquivo in os.listdir(origem) if "parte" in arquivo.lower()}          
        
        arquivos_destino = set(os.listdir(destino))
        
        
        arquivos_para_copiar = arquivos_origem - arquivos_destino
        
        if arquivos_para_copiar:
            print(f"Copiando {len(arquivos_para_copiar)} arquivo(s) para {destino}...\n")
        
        for arquivo in arquivos_para_copiar:
            origem_arquivo = os.path.join(origem, arquivo)
            destino_arquivo = os.path.join(destino, arquivo)
            
        
            if os.path.isfile(origem_arquivo):
                shutil.copy2(origem_arquivo, destino_arquivo)
                print(f"Arquivo copiado: {arquivo}")

        print("Verificação concluída!\n")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    while True:
        sincronizar_arquivos()
        time.sleep(90)
# time sleep de 1 min e 30 segundos, para que seja processado alguns arquivos primeiro e depois comece a verificação e cópia para o destino.
