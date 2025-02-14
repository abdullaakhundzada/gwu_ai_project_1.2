def read_input_file(filename):
    """
    Reads input file, and parses capacities and target

    Args:
        filename : str
            path to the input text file
    """
    with open(filename, 'r') as f:
        capacities_line = f.readline().strip()
        target_line = f.readline().strip()

        capacities = []
        if capacities_line:
            capacities = [int(c) for c in capacities_line.split(',')]
        target = int(target_line)
    return capacities, target