#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import sys # for taking variants file as input

# Define the GTEx REST API endpoint
api_url = "https://gtexportal.org/rest/v1"

# or take variants file
variants_file = sys.argv[1]

# Read variants from the text file
with open(variants_file, "r") as file:
    variants = [line.strip() for line in file]

# List of variants
# variants = [
#     "rs7329174", "rs9939609", "rs5749123", "rs5753190", "rs4820865", "rs5753193", "rs5749120",
#     "rs2899151", "rs2079312", "rs7285565", "rs4820862", "rs5994317", "rs5753201", "rs5753186",
#     "rs1107844", "rs2079311", "rs764218", "rs764217", "rs2412991", "rs2267159", "rs5997676",
#     "rs5753187", "rs2097871", "rs4820863", "rs5749122", "rs11704977", "rs5753191", "rs5753192",
#     "rs60202446", "rs5997677", "rs6518702", "rs11702947", "rs2267160"
# ]

# Initialize an empty DataFrame to store the results
result_df = pd.DataFrame(columns=["CHR", "POS", "Variant", "Variant_id", "Tissue", "Gene_id", "Gene", "Gene_upper", "nes", "P-Value"])

# Loop through each variant and make API requests
for variant in variants:
    # Make a request to get the association data for the variant
    url = f"{api_url}/association/singleTissueEqtl"
    params = {
        "format": "json",
        "snpId": variant,
        "datasetId": "gtex_v8"
    }
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Extract relevant information from the response
        for result in data["singleTissueEqtl"]:

            chromosome = result["chromosome"]
            position = result["pos"]
            variant_id = result["variantId"]
            gene_id = result["gencodeId"]
            gene = result["geneSymbol"]
            gene_upper = result["geneSymbolUpper"]
            tissue = result["tissueSiteDetailId"]
            nes = result["nes"]
            p_value = result["pValue"]

            # Append the data to the DataFrame
            result_df = result_df.append({"CHR": chromosome, "POS": position, "Variant": variant, "Variant_id": variant_id, "Tissue": tissue, "Gene_id": gene_id, "Gene": gene, "Gene_upper": gene_upper, "nes": nes, "P-Value": p_value}, ignore_index=True)
    else:
        print(f"Error fetching data for variant {variant}")

# Save the results to an Excel sheet
result_df.to_excel("20-Nov-23_query_gtex_results_haplotype_variants.xlsx", index=False)