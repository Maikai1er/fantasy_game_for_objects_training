# trying
# to
# create
# 5
# x5
# with just cycles


matrix = []

for i in range(20):
    row = []
    for j in range(20):
        row.append(0)
    matrix.append(row)

print(matrix)

new_matrix = '\n'.join(str(matrix) for matrix in matrix)

# print(new_matrix)