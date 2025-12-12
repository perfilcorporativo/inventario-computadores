import platform
import psutil
import socket
import uuid
import csv
from datetime import datetime

def coletar_informacoes():
    dados = {}

    # Nome da máquina e usuário
    dados["Hostname"] = platform.node()
    dados["Usuario"] = psutil.users()[0].name if psutil.users() else "Desconhecido"

    # Sistema Operacional
    dados["Sistema"] = platform.system()
    dados["Versao_SO"] = platform.version()

    # Processador e memória
    dados["Processador"] = platform.processor()
    dados["RAM_Total_GB"] = round(psutil.virtual_memory().total / (1024**3), 2)

    # Disco
    disco = psutil.disk_usage('/')
    dados["Disco_Total_GB"] = round(disco.total / (1024**3), 2)
    dados["Disco_Livre_GB"] = round(disco.free / (1024**3), 2)

    # IP e MAC
    dados["Endereco_IP"] = socket.gethostbyname(socket.gethostname())
    dados["MAC_Address"] = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                                     for ele in range(0, 8*6, 8)][::-1])

    # Testar internet
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        dados["Internet"] = "Conectado"
    except:
        dados["Internet"] = "Desconectado"

    # Data/Hora
    dados["Data_Hora"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return dados


def salvar_csv(dados):
    arquivo = "inventario.csv"
    
    # Cabeçalho
    campos = list(dados.keys())

    try:
        existe = False
        try:
            with open(arquivo, "r", newline='', encoding="utf-8"):
                existe = True
        except FileNotFoundError:
            existe = False

        with open(arquivo, "a", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)

            # Se for a primeira vez, escreve o cabeçalho
            if not existe:
                writer.writeheader()

            writer.writerow(dados)

        print("✔ Inventário salvo com sucesso em 'inventario.csv'")
    except Exception as erro:
        print(f"❌ Erro ao salvar: {erro}")


def main():
    print("\n📦 Coletando informações do computador...\n")
    
    dados = coletar_informacoes()
    
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

    salvar_csv(dados)


if __name__ == "__main__":
    main()
