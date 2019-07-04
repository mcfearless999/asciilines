import sys
import os

#check args
if len(sys.argv) < 2:
    print("error, file not found")
    quit()

else:
    file_name = sys.argv[1]

# create 2d matrix
def createMat(raw_size):
    sizes = raw_size.split(' ')
    if len(sizes) != 2:
        return None
    matrix = []
    v = int(sizes[0])
    h = int(sizes[1])
    for i in range(0,v):
        matrix.append([])
    for j in range(0,v):
        for k in range(0,h):
            matrix[j].append('.')
    return matrix

#print matrix
def stringify(matr):
    out_string = ""
    v = len(matr)
    h = len(matr[0])
    for i in range (0,v):
        for j in range (0,h):
            out_string += matr[i][j]
        out_string += '\n'
    return out_string

def place_line(line, matrix):
    specs = line.split(' ')
    char = specs[0]
    bound_y = len(matrix) - 1
    bound_x = len(matrix[0]) - 1
    y_pos = int(specs[1])
    x_pos = int(specs[2])
    matrix[y_pos][x_pos] = char
    ori = specs[3]
    length = int(specs[4])
    if ori == 'h':
        for i in range (0,length):
            new_x = check_bounds(x_pos + i, bound_x)
            matrix[y_pos][new_x] = char
    if ori == 'v':
        for j in range (0,length):
            new_y = check_bounds(y_pos + j, bound_y)
            matrix[new_y][x_pos] = char

def check_bounds(loc,bound):
    if loc < 0:
        return 0
    if loc > bound:
        return bound
    else:
        return loc

#read tvg file
ext = file_name[len(file_name)-4:]
if ext != ".tvg":
    quit()
file = open(file_name, 'r')
line = file.readline()
matrix = createMat(line)
if matrix == None:
    quit()
# make line
for line in file:
    place_line(line,matrix)

out_file_name = file_name.replace(ext, ".out")
out_file_name = os.getcwd() + "/tests/" + out_file_name
out_file = open(out_file_name,'w')
out_file.write(stringify(matrix))

#print (stringify(matrix))

#parse file

# write to file
