"""
Objective
- Simulate a dance between two characters
- Each character has its own set of dance moves and the combination of the moves create various magical effects.
- The goal is to determine the state of the forest after the dance is complete
"""

"""
Specifications
- Each creature can perform one of the three dance moves: 'twirl', 'leap', 'spin'
- These are the following combinations:
-- twirl + twirl = fireflies light up the forest
-- leap + spin = gentle rain starts falling
-- spin + leap = a rainbow appears in the sky
-- twirl + leap = the sun shines brightly
-- leap + twirl = the flowers die
-- spin + spin = the wind blows the leaves off the trees
-- leap + leap = a tornado forms

- Dance dynamics:
-- Each effect will change the state of the forest
-- some effects can be beneficial, while others can be harmful

- Dance Sequence:
-- the dance consists of 5 sequences
-- we need to display the state of the forest after each sequence
"""
# Call the dance function and pass in the moves of the Lox and the moves of the Faelis
lox_moves = ['twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl']
faelis_moves = ['spin', 'twirl', 'leap', 'leap', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin', 'twirl', 'leap', 'twirl', 'spin', 'spin', 'twirl', 'leap', 'spin']


# Create a function takes each dance move in the sequence for each character and returns the state of the forest after each sequence.
# The function should take two parameters: the moves of the Lox and the moves of the Faelis
# The function should return the state of the forest after each sequence
def dance(lox_dance_moves, faelis_dance_moves):
    # Define the state of the forest
    forest_states = []

    # Define the dance move combinations and their corresponding forest states
    dance_combinations = {
        ('twirl', 'leap'): 'The sun shines brightly ☀️',
        ('leap', 'spin'): 'Gentle rain starts falling 🌧️',
        ('spin', 'leap'): 'A rainbow appears in the sky 🌈',
        ('twirl', 'twirl'): 'Fireflies light up the forest 🪲',
        ('twirl', 'spin'): 'The flowers die 🌹☠️',
        ('spin', 'spin'): 'The wind blows the leaves off the trees 🌲💨🍃',
        ('leap', 'leap'): 'A tornado forms 🌪️'
    }

    # Create a for loop to iterate through the dance sequence
    for i in range(len(lox_dance_moves)):
        lox_move = lox_dance_moves[i]
        faelis_move = faelis_dance_moves[i]

        # Determine the forest state based on the dance move combination
        forest_state = dance_combinations.get((lox_move, faelis_move), 'Normal ☮️')
        forest_states.append(forest_state)

    # Return the state of the forest
    return forest_states

forest_states = dance(lox_moves, faelis_moves)

# Print the state of the forest after each sequence
for state in forest_states:
    print(state)



