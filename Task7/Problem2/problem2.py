def conditional_probability(event_a, event_b):
    if len(event_a) != len(event_b):
        raise ValueError("The events must have the same number of occurrences.")

    count_and_b = 0
    count_b = 0

    for a, b in zip(event_a, event_b):
        if b == 1:
            count_b += 1
            if a == 1:
                count_and_b += 1

    if count_b != 0:
        probability_res = count_and_b / count_b
        return probability_res
    else:
        return 0



event_a = [1, 0, 1, 0, 1]
event_b = [1, 1, 0, 0, 1]

try:
    conditional_prob = conditional_probability(event_a, event_b)
    print( conditional_prob)
except ValueError as e:
    print("Error:", e)
