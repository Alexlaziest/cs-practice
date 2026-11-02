from tablestats import read_rows, count_types, total_minutes, to_csv
name = input()
with open(name, encoding="utf-8") as f:
    rows= read_rows(f)

