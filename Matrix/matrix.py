class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string
        
    def row(self, index):
        row = (self.matrix.split('\n')[index -1]).split()
        row1 = [int(row[i]) for i in range(len(row))]
        return row1
    
        

    def column(self, index):
        column = list()
        for i in (self.matrix.split('\n')):
            column.append(int(i.split()[index-1]))
        return column 