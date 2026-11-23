<<<<<<< HEAD

=======
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
>>>>>>> 1a5797978d175f8c5824c7d85a9af3b52881c698
