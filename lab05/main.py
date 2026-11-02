from tablestats import read_rows, count_types, total_minutes, to_csv
name = input()
with open(name, encoding="utf-8") as f:
    rows= read_rows(f)
counts =count_types(rows)
print(len(rows))
print(len(counts))
print(total_minutes(rows, "ошибка"))
with open("summary.csv", "w", encoding="utf-8") as summ:
    summ.write(to_csv(counts))
