import pandas as pd

INPUT_FILE = 'DATA/AGGDATA.csv'
OUTPUT_FILE = 'DATA/AGGDATA_cleaned.csv'

# Load CSV with latin1 encoding for compatibility
raw = pd.read_csv(INPUT_FILE, encoding='latin1')

# Facility identifying columns (all columns except product information)
facility_cols = [
    'District', 'Facility Type', 'Material Type', 'Mine',
    'Facility Description', 'Company', 'Contact Person', 'Contact Email',
    'Telephone Number', 'Physical Address', 'P-Address City',
    'P-Address State', 'P-Address Zip', 'P-Address Country',
    'Latitude', 'Longitude', 'Facility Status'
]

# Aggregate duplicate facilities while combining product descriptions
aggregated = (
    raw.groupby(facility_cols, as_index=False, dropna=False)
       .agg({'Products.Description':
             lambda x: '; '.join(sorted({str(v).strip() for v in x
                                         if pd.notna(v) and str(v).strip()}))})
)

# Ensure column order matches original
aggregated = aggregated[facility_cols + ['Products.Description']]
aggregated.to_csv(OUTPUT_FILE, index=False, encoding='latin1')
print(f"Wrote {len(aggregated)} rows to {OUTPUT_FILE}")
