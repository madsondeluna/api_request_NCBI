## Descrição do Script

Este script é simples e direto, projetado para buscar e organizar dados de SNPs de forma eficiente. Seu objetivo é fornecer uma maneira fácil de acessar e visualizar informações detalhadas sobre SNPs, facilitando a análise e interpretação dos dados genéticos.

# SNP Data Fetcher - NCBI API TEST

Este repositório contém um script Python que utiliza a API do NCBI para buscar informações sobre SNPs (Polimorfismos de Nucleotídeo Único). O código acessa o banco de dados dbSNP da NCBI, obtém dados sobre um SNP específico utilizando o ID do SNP, e organiza as informações em tabelas formatadas.

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
```

## Primeiros Passos

Para executar o script, siga as instruções abaixo:

1. Clone este repositório para o seu ambiente local.
2. Instale as bibliotecas necessárias utilizando o comando `pip install requests pandas`.
3. Execute o script `ncbiapirest_test.py` com o comando `python ncbiapirest_test.py`.

## Exemplo de Uso

Aqui está um exemplo de saída ao executar o script com o SNP ID 334:

```
Informações Gerais do SNP:
| Property              | Value     |
|-----------------------|-----------|
| SNP_ID                | 334       |
| CHR                   | 1         |
| POSITION              | 1234567   |
| GENE_NAME             | ABCD1     |
| GENE_ID               | 1234      |
| CLINICAL_SIGNIFICANCE | Benign    |

Tabela de Frequências Alélicas:
| Study   | Frequency |
|---------|-----------|
| Study1  | 0.1       |
| Study2  | 0.2       |
```

## Contribuindo

Se você deseja contribuir com este projeto, siga as diretrizes abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
