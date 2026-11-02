def read_rows(lines):
    sp = []
    fst=None
    for line in lines:
        line= line.strip()
        if line == "":
            continue
        linesp= [n.strip() for n in line.split(',')]
        if fst is None:
            fst=linesp
        elif len(fst) == len(linesp):
                sp.append(dict(zip(fst, linesp)))
    return sp

def count_types(rows):
    a={}
    for row in rows:
        a[row["тип"]] = a.get(row["тип"], 0)+ 1
    return a


