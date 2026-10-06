# Inventário de Computadores (Python)

Projeto de estudo em Python para coletar informações básicas de um computador e registrar os dados em CSV.

## Informações coletadas

- Nome do computador
- Usuário conectado
- Sistema operacional
- Processador
- Memória RAM
- Espaço total e livre em disco
- Endereço IP e MAC
- Status básico de conectividade
- Data e hora da coleta

## Tecnologias utilizadas

- Python 3
- psutil
- platform
- socket
- uuid
- csv

## Como executar

1. Instale o Python 3.
2. Instale o psutil:

```bash
pip install psutil
```

3. Execute:

```bash
python inventario.py
```

O script cria ou atualiza o arquivo `inventario.csv`.

## O que pratiquei

O objetivo foi praticar automação simples, coleta de informações do sistema, organização de dados e geração de arquivos CSV.

> Projeto pessoal de estudo e portfólio. Não representa experiência profissional.
