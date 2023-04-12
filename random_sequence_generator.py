import time

# The length of the pseudo-random sequence
SEQUENCE_LENGTH = 10

# The initial seed for the pseudo-random sequence. If set to 0 or False, the current timestamp is used.
SEED_INIT = 1681304991941

# The maximum number in the sequence.
MAX_NUM = 100  

def timestamp_to_seed():
    """
    Generates a seed value based on the current timestamp.

    Returns:
    The seed value as an integer.
    """
    return int(time.time() * 1000)


def pseudo_random(seed, length):
    """
    Generates a pseudo-random sequence of integers based on a seed value.

    Args:
    - seed: The initial seed value as an integer.
    - length: The length of the sequence as an integer.

    Returns:
    The pseudo-random sequence as a list of integers.
    """
    sequence = []
    for i in range(length):
        # The formula for generating the next number in the sequence.
        seed = (1103515245 * seed + 12345) % (2 ** 31)
        sequence.append(seed % MAX_NUM)  # We take the modulus of the seed to get a number between 0 and MAX_NUM - 1.
    return sequence


# If the SEED_INIT value is set, use it as the initial seed, otherwise generate one based on the current timestamp.
if SEED_INIT:
    my_seed = SEED_INIT
else:
    my_seed = timestamp_to_seed()

# Generate the pseudo-random sequence based on the initial seed and the desired length.
my_sequence = pseudo_random(my_seed, SEQUENCE_LENGTH)

# Print out the initial seed and the generated sequence.
print("Seed : " + str(my_seed))
print(my_sequence)
