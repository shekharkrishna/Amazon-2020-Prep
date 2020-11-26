# This file contains two definitions for encoding and decoding they can be used interchangeably


# ---- The Traditional implementation ----

def encode(m):
    x1 = (m[0] ^ m[1] ^ m[3])
    x2 = (m[0] ^ m[2] ^ m[3])
    x3 = (m[1] ^ m[2] ^ m[3])
    return m + [x1, x2, x3]


def decode(m):
    x1 = (m[0] ^ m[1] ^ m[3])
    x2 = (m[0] ^ m[2] ^ m[3])
    x3 = (m[1] ^ m[2] ^ m[3])

    if x1 != m[4]:
        if x2 != m[5]:
            if x3 != m[6]:
                m[3] ^= 1
            else:
                m[0] ^= 1
        elif x3 != m[6]:
            m[1] ^= 1
        else:
            m[4] ^= 1
    elif x2 != m[5]:
        if x3 != m[6]:
            m[2] ^= 1
        else:
            m[5] ^= 1
    elif x3 != m[6]:
        m[6] ^= 1

    return m[0:4]


# ---- Matrix definition ----
# Used for part 2
# This implementation shows an alternative encoding and decoding procedure
# This is more of a proof of concept as it is almost always computationally slower to use the matrix definition.
# Instead optimizations should be made, like not calculating the first 4 bits.
# The implementation above is a perfect example of an optimized implementation of what is shown here
# You might ask why this is important if we don't use it? This definition is really important for the math behind decoding and not the actual implementation.


import numpy as np


generator_matrix = np.array([[1, 0, 0, 0, 1, 1, 0],
                             [0, 1, 0, 0, 1, 0, 1],
                             [0, 0, 1, 0, 0, 1, 1],
                             [0, 0, 0, 1, 1, 1, 1]])


parity_check_matrix = np.array([[1, 1, 0, 1, 1, 0, 0],
                                [1, 0, 1, 1, 0, 1, 0],
                                [0, 1, 1, 1, 0, 0, 1]])


def encode_matrix(m):
    # A bit of conversion needs to be done
    # Taking the mod 2 here is the same as using XOR over normal addition
    return (np.array([m], dtype=np.bool).dot(generator_matrix) % 2).tolist()[0]


def decode_matrix(m):
    # There are more optimized methods of doing this
    # Calculate syndrome
    syndrome = (np.array([m], dtype=np.bool).dot(parity_check_matrix.transpose()) % 2)
    if not syndrome.any():
        return m[0:4]
    syndrome = syndrome.tolist()[0]

    # Search for the syndrome in the list
    pc_matrix = parity_check_matrix.transpose().tolist()
    err_ind = pc_matrix.index(syndrome)

    # Fix error
    m[err_ind] ^= 1
    return m[0:4]