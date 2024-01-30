# two_sample_MR
A two-sample Mendelian randomization analysis during Dianne's stay at Eurac Research

#### Filtering variants using GTEx v.8
- The genes were looked up across summary stats of the deCODE study to find the pQTL variants in each gene (Tue 18:30, 14-Nov-23).

- The filtered variants were queried on GTEx v.8 and the resulting eQTLs were stored (Thu 16:30, 16-Nov-23).

- Practical example of one-sample MR postponed to Monday (18:20, 17-Nov-23).

- Git version control was convered. In addtion, we queried the variants in other genes in GTEx for tissue specific eQTLs for the vicinity genes (Mon, 19:00, 20-Nov-23).

- The identified eQTL varinats were extracted from the CKDGen GWAS meta-analyis summary stats on eGFRcrea Overal (build 37) (Tue, 17:40, 21-Nov-23)!

### Preliminary results for two sample MR

- For Ele, we used dynamic QTL endpoint of GTEX API V2 to find variant-gene expression of the interested genes being used for mendelian randomization using `03_query_gtex_genome.py` (Tue, 19:30, 30-Jan-24).

-Dariush-