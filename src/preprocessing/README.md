This folder contains all notebooks written using R language to download the GEO datasets from NCBI and 
make a preliminary analysis.

The preliminary is a pipeline that:

1. Downloads the dataset
2. Filters out the "homo-sapiens" records
3. Selects the correct samples (e.g. the patients that are affected)
4. Converts the GeneSymbol to standard convention.