def printTable(list):
    maxLong = []

    for i in range(len(tableData)):
        max = 0
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > max:
                max = len(tableData[i][j])
        maxLong.append(max)

    for line in range(len(tableData[0])):
        for colum in range(len(tableData)):
            print(tableData[colum][line].rjust(maxLong[colum]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana', 'coco', 'icecream'],
             ['Alice', 'Bob', 'Carol', 'David', 'Anna', 'Penelope'],
             ['dogs', 'cats', 'moose', 'goose', 'snakes', 'monkeys']]

printTable(tableData)
