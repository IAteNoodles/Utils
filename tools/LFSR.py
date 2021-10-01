class LFSR:
    """
    Linear Feedback Shift Register
    """

    def __init__(self, seed: float):
        self.__SEED = seed
        self.__SEEDLET = 0b0000


    def generate_sequence(self):
        state = 0b00011111  # Given state
        state_length = state.bit_length()   # Stores the bit length of the state
        dataset = [bin(state)]
        while True:  # Loops until dataset has all the possible states for a given combination of bits
            new_bit = (state ^ (state >> 1)) & 1
            state = (state >> 1) | (new_bit << state_length)
            print("{:04b}".format(state))
            self.__SEEDLET = self.__SEEDLET << 1 | new_bit
            if bin(state) not in dataset:
                dataset.append(bin(state))
                print(bin(self.__SEEDLET))
            else:
                break


LFSR(1562.156).generate_sequence()
