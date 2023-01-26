# Open input file
with open("SVV-zit22-vvod.txt", "r") as input_file:
    # Get matrix size from file
    size = int(input_file.readline())

    # Throw an error if size is not a natural number
    if size <= 0:
        raise ValueError

    count = 0
    result = 0

    for row in range(size):
        # Get row and convert it into list
        array = [int(x) for x in input_file.readline().split()]

        # For loop through row
        for col in range(size):
            # If item belongs to main diagonal or lies below, skip it
            if col <= row:
                continue

            # If item is negative, skip it
            if array[col] < 0:
                continue

            # Add item to result and increase count value by 1
            result += array[col]
            count += 1

# Open output file
with open("SVV-zit22-vivod.txt", "w") as output_file:
    # Output to file
    output_file.write(f"Found {count} positive items above main diagonal;\n")
    output_file.write(f"Sum of all positive items: {result}.")
