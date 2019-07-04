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

#read tvg file

file = open(file_name, 'r')

matrix = createMat(file.read())
if matrix == None:
    quit()
print (stringify(matrix))

#parse file


# make line
# write to file
