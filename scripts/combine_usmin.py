import csv
import glob
import os
import re
import shapefile


def combine(type_="point"):
    pattern = "usmin-*.zip"
    out_dir = "DATA"
    os.makedirs(out_dir, exist_ok=True)
    if type_ == "point":
        csv_name = "usmin_points.csv"
    else:
        csv_name = "usmin_polygons.csv"
    csv_path = os.path.join(out_dir, csv_name)

    writer = None
    outfile = None
    for zip_path in sorted(glob.glob(pattern)):
        m = re.search(r"usmin-([A-Z]{2})", os.path.basename(zip_path))
        if not m:
            continue
        state = m.group(1)
        shp_name = f"{state}-{type_}.shp"
        shp_path = f"{zip_path}/{shp_name}"
        try:
            sf = shapefile.Reader(shp_path)
        except Exception:
            # Skip if shapefile not present
            continue
        fields = [f[0] for f in sf.fields[1:]]
        if writer is None:
            header = fields + ["LONGITUDE", "LATITUDE", "STATE"]
            outfile = open(csv_path, "w", newline="", encoding="utf-8")
            writer = csv.writer(outfile)
            writer.writerow(header)
        for sr in sf.iterShapeRecords():
            row = list(sr.record)
            lon, lat = sr.shape.points[0]
            row += [lon, lat, state]
            writer.writerow(row)
    if outfile:
        outfile.close()


def main():
    combine("point")
    combine("poly")


if __name__ == "__main__":
    main()
