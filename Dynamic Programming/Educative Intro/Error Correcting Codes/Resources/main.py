# To use this file simply click run.
# It will automatically encode and decode a user inputted bit string
# View hamming.py for implementations
import hamming
import random

# Two helper functions
def split(lst, size):
    res = []
    for i in range(0, len(lst), size):
        res.append(lst[i:i + size])
    if len(res[-1]) < size:
        res[-1] = res[-1] + [0]*(size-len(res[-1]))
    return res


def sim_error(msg, p_err=float(1/15)):
    res = [None]*len(msg)
    for m in range(len(res)):
        if random.random() < p_err:
            res[m] = msg[m] ^ 1
        else:
            res[m] = msg[m]

    return res


# To change the probability of error change this value
prob_err=float(1/12)


# With the input we will add 0's the end to ensure we have groups of 4.
a = list(input("Enter a bit string: "))
a = [int(j) for j in a]
a = split(a, 4)

print(f"Original Message:           {[j for sub in a for j in sub]}")

# Encode the messages
encoded_msg = []
for j in range(len(a)):
    encoded_msg += hamming.encode(a[j])

# Simulate error
err_msg = sim_error(encoded_msg, p_err=prob_err)

print(f"Encoded Message:            {encoded_msg}\n")
print(f"Encoded Message with error: {err_msg}")
print(f"The Error:                  {[j ^ k for j, k in zip(encoded_msg, err_msg)]}\n")

# Decode
err_msg_chuncked = split(err_msg, 7)
decoded_msg = []
for j in range(len(err_msg_chuncked)):
    decoded_msg += hamming.decode(err_msg_chuncked[j])

print(f"Decoded Message:            {decoded_msg}")
print(f"Decoded Correctly: {decoded_msg == [j for sub in a for j in sub]}")