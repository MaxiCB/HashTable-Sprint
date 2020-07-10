def get_indices_of_item_weights(weights, length, limit):
    # Weights - [item_weight] - Int[]
    # Limit - Weight Limit - Int
    # Requirements
    # Given a weight limit
    # Chose two items from weights
    # Who's sum equals the limit

    cache = dict()

    for i in range(len(weights)):
        # Current weight value
        cw = weights[i]
        # Check if already in cache
        if cw in cache:
            # If in cache grab it's counterpart
            seen = cache[cw]
            # Creation of the output tuple
            output = (i, seen)
            return output

        # Insert Current Item Into Cache
        # Key: Remainder needed for limit
        # Value: Item Index
        cache[limit - cw] = i

    return None
