import sys

# input file
with open(sys.argv[1]) as f:
    data = [list(map(int, str(x)))
            for x in [line.strip() for line in f.readlines()]]

# Check Size
rowLength = len(data)
columnLength = len(data[0])
ans = 0


def checkObstacle(row, column):
    global ans
    # Check border
    if row in [0, rowLength - 1] or column in [0, columnLength - 1]:
        ans += 1
        return
    # Check inside
    else:
        count = 0
        # Check top
        for _row in range(row):
            if data[_row][column] >= data[row][column]:
                count += 1
                break
            if _row == (row - 1):
                ans += 1
                return
        # Check Left
        for _column in range(column):
            if data[row][_column] >= data[row][column]:
                count += 1
                break
            if _column == (column - 1):
                ans += 1
                return
        # Check Bottom
        for _row in range(row + 1, rowLength):
            if data[_row][column] >= data[row][column]:
                count += 1
                break
            if _row == (rowLength - 1):
                ans += 1
                return
          # Check Right
        for _column in range(column + 1, columnLength):
            if data[row][_column] >= data[row][column]:
                count += 1
                break
            if _column == (columnLength - 1):
                ans += 1
                return

for row in range(rowLength):
    for column in range(columnLength):
      checkObstacle(row, column)



print(ans)
