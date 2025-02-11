import csv
import random
from faker import Faker
import os

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
valor_total_estoque = 0

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
        valor_total_estoque += (
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
print(f"Valor total do estoque: R$ {round(valor_total_estoque, 2)}")
