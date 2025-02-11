"""
Este script gera um arquivo CSV contendo uma lista fictícia de itens de estoque.

O script solicita ao usuário o nome do arquivo CSV a ser gerado e a quantidade 
de itens fictícios a serem criados.  Em seguida, ele gera dados aleatórios para
 cada item, incluindo ID do produto, nome, categoria, quantidade em estoque,
preço unitário, valor agregado, data de aquisição, fornecedor, localização no 
armazém, número de série, status, data de validade e observações.

Bibliotecas utilizadas:
- csv: para manipulação de arquivos CSV.
- random: para geração de valores aleatórios.
- faker: para geração de dados fictícios.
- os: para manipulação de caminhos de arquivos.

Classes e funções:
- Nenhuma classe ou função específica é definida neste script.

Variáveis:
- fake: instância da classe Faker para geração de dados fictícios.
- produtos: lista de nomes de produtos.
- categorias: lista de categorias de produtos.
- status_opcoes: lista de status possíveis para os produtos.
- output_file: nome do arquivo CSV fornecido pelo usuário.
- num_itens: quantidade de itens fictícios a serem gerados, fornecida pelo usuário.
- valor_total_estoque: variável para acumular o valor total do estoque.

Fluxo do script:
1. Solicita ao usuário o nome do arquivo CSV e a quantidade de itens a serem gerados.
2. Inicializa a variável valor_total_estoque.
3. Cria e escreve no arquivo CSV com os dados fictícios gerados.
4. Exibe o caminho absoluto do arquivo gerado e o valor total do estoque.

Como usar:
1. Execute o script.
2. Insira o nome do arquivo CSV quando solicitado.
3. Insira a quantidade de itens fictícios a serem gerados.
4. O script gerará o arquivo CSV com os dados fictícios e exibirá o caminho do 
arquivo e o valor total do estoque.

Exemplo de uso:
$ python fakerestoque.py
Digite o nome do arquivo .csv (ex: estoque.csv): estoque.csv
Quantidade de itens fictícios a serem criados: 10
Arquivo 'estoque.csv' gerado com sucesso! Caminho: /caminho/para/estoque.csv
Valor total do estoque: R$ 123456.78
"""
import csv
import os
import random
from faker import Faker


# Criar instância do Faker
fake = Faker("pt_BR")

# Definir listas de produtos e categorias
produtos = [
    "Notebook",
    "Smartphone",
    "Tablet",
    "Monitor",
    "Teclado",
    "Mouse",
    "Impressora",
    "Scanner",
    "Câmera",
    "Fone de Ouvido",
]
categorias = ["Equipamentos Eletrônicos", "Acessórios", "Periféricos"]
status_opcoes = ["Disponível", "Em Uso", "Em Manutenção", "Descartado"]

# Solicitar informações ao usuário
output_file = input("Digite o nome do arquivo .csv (ex: estoque.csv): ")
num_itens = int(input("Quantidade de itens fictícios a serem criados: "))

# Inicializar variável para acumular o valor total do estoque
VALOR_TOTAL_ESTOQUE = 0

# Criar e escrever no arquivo CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    nomes_colunas = [
        "ID do Produto",
        "Nome do Produto",
        "Categoria",
        "Quantidade em Estoque",
        "Preço Unitário",
        "Valor Agregado",
        "Data de Aquisição",
        "Fornecedor",
        "Localização no Armazém",
        "Número de Série",
        "Status",
        "Data de Validade",
        "Observações",
    ]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=nomes_colunas)
    escritor.writeheader()

    for i in range(
        1, num_itens + 1
    ):  # Gerar a quantidade de itens especificada pelo usuário
        produto = random.choice(produtos)
        categoria = random.choice(categorias)
        quantidade = random.randint(1, 50)
        preco_unitario = round(random.uniform(100.0, 10000.0), 2)
        valor_agregado = quantidade * preco_unitario
        VALOR_TOTAL_ESTOQUE += (
            valor_agregado  # Acumular o valor agregado no valor total do estoque
        )
        escritor.writerow(
            {
                "ID do Produto": i,
                "Nome do Produto": produto,
                "Categoria": categoria,
                "Quantidade em Estoque": quantidade,
                "Preço Unitário": preco_unitario,
                "Valor Agregado": round(valor_agregado, 2),
                "Data de Aquisição": fake.date_between(
                    start_date="-2y", end_date="today"
                ),
                "Fornecedor": fake.company(),
                "Localização no Armazém": f"Seção {random.randint(1,10)} - Prateleira {random.randint(1,5)}",
                "Número de Série": (
                    fake.unique.ean13()
                    if categoria == "Equipamentos Eletrônicos"
                    else ""
                ),
                "Status": random.choice(status_opcoes),
                "Data de Validade": (
                    fake.date_between(start_date="today", end_date="+3y")
                    if "Bateria" in produto
                    else ""
                ),
                "Observações": "",
            }
        )

# Obter o caminho absoluto do arquivo salvo
file_path = os.path.abspath(output_file)
print(f"Arquivo '{output_file}' gerado com sucesso! Caminho: {file_path}")
print(f"Valor total do estoque: R$ {round(VALOR_TOTAL_ESTOQUE, 2)}")
