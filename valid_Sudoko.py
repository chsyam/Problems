def display(sudoko):
    for i in sudoko:
        print(*i)

def rows(sudoko):
    return sudoko

def cols(sudoko):
    col_matrix = []
    for i in range(9):
        line = []
        for j in range(9):
            line.append(sudoko[j][i])
        col_matrix.append(line)
    return col_matrix
    
def boxes(sudoko):
    box_matrix = []
    for i in range(1,9,3):
        for j in range(1,9,3):
            l = [sudoko[i-1][j-1], sudoko[i-1][j], sudoko[i-1][j+1]]
            l += [sudoko[i][j-1], sudoko[i][j], sudoko[i][j+1]]
            l += [sudoko[i+1][j-1], sudoko[i+1][j], sudoko[i+1][j+1]]
            box_matrix.append(l)
    return box_matrix


def valid(box_matrix,col_matrix,row_matrix):
    for i in range(9):
        d1,d2,d3 = {},{},{}
        for j in box_matrix[i]:
            if j not in d1:
                d1[j] = 1
            else:
                d1[j] += 1
        for j in col_matrix[i]:
            if j not in d2:
                d2[j] = 1
            else:
                d2[j] += 1
        for j in row_matrix[i]:
            if j not in d3:
                d3[j] = 1
            else:
                d3[j] += 1
        for j in d1:
            if d1[j] > 1 and j!=".":
                return False
        for j in d2:
            if d2[j] > 1 and j!=".":
                return False
        for j in d3:
            if d3[j] > 1 and j!=".":
                return False
    return True


sudoko = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."], 
        ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
        [".", "9", "8", ".", ".", ".", ".", "6", "."], 
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
        [".", "6", ".", ".", ".", ".", "2", "8", "."], 
        [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

row_matrix = rows(sudoko)
col_matrix = cols(sudoko)
box_matrix = boxes(sudoko)

print(valid(box_matrix,col_matrix,row_matrix))