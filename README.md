# AGGMap2.0

This repository contains data and utilities for processing aggregate facility information.

## Files

CSV data files are stored in the `DATA` directory:

- `DATA/AGGDATA.csv` – Raw facility data exported from LIMS.
- `DATA/AGGDATA_cleaned.csv` – Deduplicated records used by the map interface.
- `DATA/Approved Products.csv` – Approved products list.
- `DATA/All ProducersNot.csv` – Producer information.

Other repository files:
- `index.html` – Prototype web map interface that loads `DATA/AGGDATA_cleaned.csv` by default.
- `merge_duplicates.py` – Utility script that merges duplicate facility records.

## Merging Duplicate Rows

Some facilities appear multiple times in `AGGDATA.csv` with identical attributes but different product descriptions. Run the merge script to combine these entries and create `AGGDATA_cleaned.csv`:

```bash
python3 merge_duplicates.py
```

The script groups rows by coordinates and facility details, then collapses the `Products.Description` values into a single `;`‑separated list for each facility.
