import sys


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
    return out_string.rstrip()

def place_line(line, matrix):
    specs = line.split(' ')
    char = specs[0]
    y_pos = int(specs[1])
    x_pos = int(specs[2])
    matrix[y_pos][x_pos] = char




#read tvg file
ext = file_name[len(file_name)-4:]
if ext != ".tvg":
    quit()
file = open(file_name, 'r')
line = file.readline()
matrix = createMat(line)

# make line
for line in file:
    place_line(line,matrix)

if matrix == None:
    quit()
print (stringify(matrix))

#parse file

# write to file
