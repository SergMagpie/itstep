def pascal_trianngle(row_count):
    
    triangle=[1]
    if row_count>1:
        triangle.append([1,1])
        for n_row in range(1,row_count):
            row=[1]+[triangle[n_row][n]+triangle[n_row][n+1]
                     for n in range(len(triangle[n_row])-1)]+[1]
            triangle.append(row)
    return triangle

[print(str(x).center(80)) for x in list(pascal_trianngle(10))]
