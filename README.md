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
- `Icons/` – Contains image assets used by the map such as the aggregate supplier pin.

## USMIN Data

The repository also includes USMIN mineral occurrence data packaged by state. The
`scripts/combine_usmin.py` utility extracts the point and polygon shapefiles from
each `usmin-??.zip` archive and concatenates them into combined CSV files. Run:

```bash
python scripts/combine_usmin.py
```

This command will produce `DATA/usmin_points.csv` and `DATA/usmin_polygons.csv`
containing all records with an additional `STATE` column derived from the
archive names.

