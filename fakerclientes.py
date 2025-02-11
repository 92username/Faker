# cria um arquivo com dados falsos com output em formato csv
import csv
from faker import Faker
from random import choice
import os

# Solicitar informações ao usuário
output_file = os.path.join(
    "arquivos_csv", input("Digite o nome do arquivo .csv (ex: clientes.csv): ")
)
NUM_PF = int(input("Quantidade de Pessoas Físicas a serem criadas: "))
NUM_PJ = int(input("Quantidade de Pessoas Jurídicas a serem criadas: "))

clientes = []

# Criar instância do Faker com locale pt_BR
faker = Faker("pt_BR")

# Gerar clientes pessoa física
for i in range(1, NUM_PF + 1):
    cliente = {
        "ID": i,
        "Nome": faker.name(),
        "Telefone": faker.phone_number(),
        "Endereço": faker.address().replace("\n", ", "),
        "Email": faker.email(),
        "Notas": "",
        "CPF": faker.ssn(),  # Usar ssn() para CPF
        "CNPJ": "",
        "Cliente desde": f"{int(faker.month()):02d}-{faker.year()}",
        "Pagamentos": choice(["mensal", "diária"]),
        "Pagamento em dia": choice(["em dia", "em atraso"]),
    }
    clientes.append(cliente)

# Gerar clientes pessoa jurídica
for i in range(NUM_PF + 1, NUM_PF + NUM_PJ + 1):
    cliente = {
        "ID": i,
        "Nome": faker.company(),
        "Telefone": faker.phone_number(),
        "Endereço": faker.address().replace("\n", ", "),
        "Email": faker.company_email(),
        "Notas": "",
        "CPF": "",
        "CNPJ": faker.ssn(),  # Usar ssn() para CNPJ
        "Cliente desde": f"{int(faker.month()):02d}-{faker.year()}",
        "Pagamentos": choice(["mensal", "diária"]),
        "Pagamento em dia": choice(["em dia", "em atraso"]),
    }
    clientes.append(cliente)

# Escrever no arquivo CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "ID",
        "Nome",
        "Telefone",
        "Endereço",
        "Email",
        "Notas",
        "CPF",
        "CNPJ",
        "Cliente desde",
        "Pagamentos",
        "Pagamento em dia",
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(clientes)

# Obter o caminho absoluto do arquivo salvo
file_path = os.path.abspath(output_file)
print(f"Arquivo '{output_file}' gerado com sucesso! Caminho: {file_path}")
