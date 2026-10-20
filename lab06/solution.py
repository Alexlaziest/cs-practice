values = ["ошибка", "запуск", "ошибка", "проверка"]
def count_items(values):
    d= {}
    for i in values:
        d[i]= d.get(i, 0)+1
    return d
print(count_items(values))
