# aabcc to 2a1b2c

def encode(input_encode):
    # Check for null input
    if input_encode is None or len(input_encode) == 0:
        return " "
    sb = []
    counter = 0
    prev_char = None
    # iterate over input
    for char in input_encode:
        if char is prev_char:
            counter += counter
        elif prev_char:
            sb.append(counter)
    prev_char = char
    counter = 1
    sb.append(counter)
    sb.append(prev_char)
    return sb

# test
input_encode = 'aabcc'
print(encode(input_encode))
