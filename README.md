# SNP Data Fetcher

Este repositório contém um script Python que utiliza a API do NCBI para buscar informações sobre SNPs (Single Nucleotide Polymorphisms). O código acessa o banco de dados dbSNP da NCBI, obtém dados sobre um SNP específico utilizando o ID do SNP, e organiza as informações em tabelas formatadas.

## Funcionalidades

- **Busca de dados de SNP**: Através do ID de SNP fornecido, o script consulta a API do NCBI e obtém um resumo dos dados em formato XML.
- **Parsing de dados XML**: Extrai informações relevantes do XML, como o ID do SNP, cromossomo, posição, nome e ID do gene associado, significância clínica e frequências alélicas.
- **Apresentação de dados**: Os dados extraídos são organizados em dois DataFrames: um para informações gerais do SNP e outro para as frequências alélicas (MAF - Minor Allele Frequency).

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `requests`: para fazer as requisições HTTP à API do NCBI.
- `xml.etree.ElementTree`: para analisar os dados XML retornados pela API.
- `pandas`: para organizar e exibir os dados de forma tabular.

Você pode instalá-las utilizando o `pip`:

```bash
pip install requests pandas
