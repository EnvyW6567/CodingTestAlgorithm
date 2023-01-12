from collections import defaultdict


def toIdx(r, c):
    return r*100 + c


def toInt(idx):
    r = int(idx/100)
    c = idx % 100
    return r, c


def removeValue(r, c, table, idxDic):

    idxDic[table[r][c]].remove([int(r), int(c)])
    table[r][c] = None
    return table, idxDic


def insertValue(r, c, value, table, idxDic):
    table[r][c] = value
    idxDic[value].append([int(r), int(c)])


def Update(command, table, idxDic):  # UPDATE 1 1 menu, UPDATE menu menu

    # Value -> Value
    if len(command == 4):
        before = command[1]
        after = command[2]
        for idx in idxDic[before]:
            idxDic[after].append(idx)
            table[idx[0]][idx[1]] = after
        idxDic[before] = []

        return table, idxDic

    r = command[1]
    c = command[2]
    value = command[3]
    table, idxDic = insertValue(r, c, value, table, idxDic)

    return table, idxDic


def Merge(command, table, idxDic):  # MERGE 1 2 1 3

    r = command[1]
    c = command[2]
    rM = command[3]
    cM = command[4]
    if table[r][c]:
        if table[rM][cM]:
            idxDic[table[rM][cM]].remove([int(rM), int(cM)])

        idxDic[table[r][c]].append([int(rM), int(cM)])
        idxDic[table[r][c]].append([int(rM), int(c)])
        idxDic[toInt(r, c)].append([int(rM), int(cM)])
        idxDic[toInt(rM, cM)].append([int(r), int(c)])

    elif table[rM][cM]:
        table[r][c] = toInt(rM, cM)
    else:

    return table, idxDic


def Unmerge(command, table):  # UNMERGE 1 4

    r = command[1]
    c = command[2]

    return table


def Print(command, table):  # PRINT 1 4

    r = command[1]
    c = command[2]

    if not table[r][c]:
        return "EMPTY"

    prt = table[r][c]
    return prt


def solution(commands):
    answer = []

    idxDic = defaultdict(list)
    table = [[None for _ in range(50)]for _ in range(50)]

    for command in commands:
        command = command.split(" ")
        func = command[0]
        if func == "UPDATE":
            table, idxDic = Update(command, table, idxDic)
        elif func == "MERGE":
            table, idxDic = Merge(command, table, idxDic)
        elif func == "UNMERGE":
            table, idxDic = Unmerge(command, table, idxDic)
        else:
            answer.append(Print(command, table))

    return answer


commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
            "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]

print(f'answer : {solution(commands)}')
