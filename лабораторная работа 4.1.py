# Open input file
with open("SVV-zit22-vvod.txt", "r") as input_file:
    # Get matrix width and height from file
    width = int(input_file.readline())
    height = int(input_file.readline())

    if width <= 0 or height <= 0:
        raise ValueError

    matrix = []

    for row in range(height):
        matrix.append([int(x) for x in input_file.readline().split()][:width])

        max_index = matrix[row].index(max(matrix[row]))
        min_index = matrix[row].index(min(matrix[row]))

        matrix[row][0], matrix[row][min_index] = matrix[row][min_index], matrix[row][0]
        matrix[row][-1], matrix[row][max_index] = matrix[row][max_index], matrix[row][-1]

    # Open output file
    with open("SVV-zit22-vivod.txt", "w") as output_file:
        # Output new matrix to file
        output_file.write("New matrix: \n")
        for row in range(height):
            output_file.write(
                " ".join([str(matrix[row][col]) for col in range(width)]) + '\n')
