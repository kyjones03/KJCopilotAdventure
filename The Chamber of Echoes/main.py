# Objective
# - Create a game where a player enters a room and listens to a series of echoes of numbers
# - The player must be able to say what the next number in the series is
# - If the player gets the number wrong, they must start over
# - If the player gets the number right, they receive access to hidden treasures

# Inputs
# - A list of at least 3 numbers that form a sequence. The list represents the numbers the room echoed in the past.

# Outputs
# - A single number representing the next number in the sequence

# Assumptions
# - The sequence will always be an arithmetic sequence (the difference between each number is constant)

echoes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
memories = []

def nextNumber(echoes):
    """
    Calculates the next number in a given arithmetic sequence based on the provided list of echoes.

    Parameters:
    echoes (list): A list of at least 3 numbers that form an arithmetic sequence.

    Returns:
    int: The next number in the arithmetic sequence.
    """
    difference = echoes[1] - echoes[0]
    nextNumber = echoes[-1] + difference
    # Store the full sequence of echoes in the memories list
    memories.extend(echoes)
    return nextNumber

print(nextNumber(echoes))
