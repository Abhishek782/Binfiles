import csv

classrowcolMap = {}
colMap = {}
rowMap = {}

with open("input.csv", mode="r") as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        row_name, col_name, count = row
        val = int(count)
        if row_name not in classrowcolMap:
            classrowcolMap[row_name] = {}
        classrowcolMap[row_name][col_name] = val
        colMap[col_name] = colMap.get(col_name, 0) + val
        rowMap[row_name] = rowMap.get(row_name, 0) + val

for r in rowMap:
    for c in colMap:
        print(f"{r}-{c}: {classrowcolMap[r][c]}")

for r in rowMap:
    print(f"{r} -> {rowMap[r]}")

for c in colMap:
    print(f"{c} -> {colMap[c]}")

colSum = sum(colMap.values())
rowSum = sum(rowMap.values())
print(f"colSum: {colSum}")
print(f"rowSum: {rowSum}")

with open("output.csv", mode="w", newline='') as fw:
    writer = csv.writer(fw)
    writer.writerow(["Column\\row", "", "Bollywood", "", "", "Tollywood", "", "", "Total", "", ""])
    writer.writerow(["", "Count", "t-weight", "d-weight", "Count", "t-weight", "d-weight", "Count", "t-weight", "d-weight"])

    for r in rowMap:
        row = r
        row_data = [row]
        for c in colMap:
            col = c
            row_data.extend([
                classrowcolMap[row][col],
                (classrowcolMap[row][col] / rowMap[row]) * 100,
                (classrowcolMap[row][col] / colMap[col]) * 100
            ])
        row_data.extend([rowMap[row], (rowMap[row] / rowMap[row]) * 100, (rowMap[row] / colSum) * 100])
        writer.writerow(row_data)

    total_row = ["Total"]
    for c in colMap:
        col = c
        total_row.extend([colMap[col], (colMap[col] / colSum) * 100, (colMap[col] / colMap[col]) * 100])
    total_row.extend([colSum, 100, 100])
    writer.writerow(total_row)
