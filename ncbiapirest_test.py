import requests
import xml.etree.ElementTree as ET
import pandas as pd

def get_snp_summary(snp_id):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=snp&id={snp_id}&retmode=xml"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        return response.text  # Retorna os dados em formato XML
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data: {e}"}

def parse_snp_data(xml_data):
    root = ET.fromstring(xml_data)

    # Procurando o nó principal
    document_summary = root.find(".//DocumentSummary")

    if document_summary is None:
        return "No data found."

    # Extraindo informações específicas
    snp_data = {}
    snp_data['SNP_ID'] = document_summary.findtext("SNP_ID_SORT")
    snp_data['CHR'] = document_summary.findtext("CHR")
    snp_data['POSITION'] = document_summary.findtext("CHRPOS")
    snp_data['GENE_NAME'] = document_summary.find(".//GENE_E/NAME").text if document_summary.find(".//GENE_E/NAME") else "N/A"
    snp_data['GENE_ID'] = document_summary.find(".//GENE_E/GENE_ID").text if document_summary.find(".//GENE_E/GENE_ID") else "N/A"
    snp_data['CLINICAL_SIGNIFICANCE'] = document_summary.findtext("CLINICAL_SIGNIFICANCE")
    snp_data['ALLELE_FREQUENCIES'] = []

    # Extraindo frequências alélicas (MAF)
    for maf in document_summary.findall(".//MAF"):
        study = maf.findtext("STUDY")
        freq = maf.findtext("FREQ")
        snp_data['ALLELE_FREQUENCIES'].append({"Study": study, "Frequency": freq})

    return snp_data

# Testar a função com o SNP ID rs334, não adicionar o "rs" ao campo
snp_id = "334"
xml_data = get_snp_summary(snp_id)
parsed_data = parse_snp_data(xml_data)

# Criando DataFrame para informações gerais
info_data = {
    "Property": ["SNP_ID", "CHR", "POSITION", "GENE_NAME", "GENE_ID", "CLINICAL_SIGNIFICANCE"],
    "Value": [
        parsed_data["SNP_ID"],
        parsed_data["CHR"],
        parsed_data["POSITION"],
        parsed_data["GENE_NAME"],
        parsed_data["GENE_ID"],
        parsed_data["CLINICAL_SIGNIFICANCE"],
    ],
}
info_df = pd.DataFrame(info_data)

# Criando DataFrame para frequências alélicas
allele_frequencies_df = pd.DataFrame(parsed_data["ALLELE_FREQUENCIES"])

# Exibindo as tabelas organizadas
print("Informações Gerais do SNP:")
print(info_df.to_markdown(index=False))

print("\nTabela de Frequências Alélicas:")
print(allele_frequencies_df.to_markdown(index=False))
