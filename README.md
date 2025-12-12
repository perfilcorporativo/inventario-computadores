# 🖥️ Inventário de Computadores (Python)

Um projeto simples e eficiente para coletar informações de hardware e sistema operacional usando Python.  
Ele gera um inventário completo contendo:

- Nome do computador
- Usuário logado
- CPU
- Memória RAM total
- Espaço total e livre do disco
- Sistema operacional (nome + versão)
- Endereço IPv4

As informações são salvas em um arquivo **inventario.csv** automaticamente.

---

## 🚀 Tecnologias utilizadas

- **Python 3**
- **psutil** (para coletar informações do sistema)
- **platform** (nativa do Python)
- **getpass** (nativa do Python)
- **csv** (nativa do Python)

▶️ Como executar o projeto

1. Abra o terminal na pasta do projeto

2. Execute o script:

python inventario.py

3. Será criado/atualizado o arquivo:

inventario.csv

### Exemplo de saída do CSV

computador,usuario,cpu,ram_total_gb,disco_total_gb,disco_livre_gb,so,ipv4
DESKTOP-1234,joao,i5-7400,8.0,465.0,123.5,Windows 10,192.168.0.12

