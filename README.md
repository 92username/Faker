# Gerador de Dados Falsos para Prototipagem

Este projeto utiliza a biblioteca [Faker](https://faker.readthedocs.io/) para gerar dados falsos de clientes em um arquivo `.csv`. Ele é útil para prototipagem de sistemas que exigem dados simulados de pessoas físicas e jurídicas.

## Descrição do Código

Este script permite gerar um arquivo `.csv` com dados falsos de clientes. É possível configurar:
- Nome do arquivo `.csv`.
- Quantidade de clientes pessoa física.
- Quantidade de clientes pessoa jurídica.

Cada registro no arquivo contém as seguintes informações:
- ID
- Nome
- Telefone
- Endereço
- Email
- Notas (campo vazio para preenchimento posterior)
- CPF (apenas para pessoas físicas)
- CNPJ (apenas para pessoas jurídicas)
- Cliente desde (mês e ano de entrada como cliente)
- Pagamentos (mensal ou diária)
- Pagamento em dia (em dia ou em atraso)

## Como Usar
Recomendado utilizar um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate
```

1. **Instale as dependências**: Execute o comando abaixo para instalar a biblioteca Faker:
   ```bash
   pip install Faker
   ```
   
2. **Execute o Script**: Rode o código com Python e siga as instruções para configurar o nome do arquivo e a quantidade de clientes.
   ```bash
   python fakerclientes.py
   ```

3. **Exemplo de Uso**:
   - Nome do arquivo: `clientes.csv`
   - Quantidade de Pessoas Físicas: 10
   - Quantidade de Pessoas Jurídicas: 15

4. **Output**:
   - O arquivo `.csv` será salvo no diretório especificado com os dados gerados.

## Estrutura do Arquivo `.csv`

| ID  | Nome            | Telefone         | Endereço                     | Email           | Notas | CPF       | CNPJ      | Cliente desde | Pagamentos | Pagamento em dia |
|-----|------------------|------------------|------------------------------|-----------------|-------|-----------|-----------|---------------|------------|-------------------|
| 1   | Nome Pessoa 1   | (99) 99999-9999  | Endereço Exemplo, 123, Cidade| exemplo@email.com |       | 123.456.789-09 |           | 01-2022      | mensal     | em dia            |
| 2   | Empresa Exemplo | (99) 88888-8888  | Rua Exemplo, 456, Cidade     | empresa@email.com |       |           | 12.345.678/0001-90 | 02-2023      | diária     | em atraso         |

## Imagens

1. **Exemplo da saída do terminal após a execução**:

  ![Terminal Output](terminaloutputfaker.png)


2. **Exemplo do arquivo `.csv` gerado**:

   ![Exemplo do arquivo CSV gerado](outputcsvfaker.png)
