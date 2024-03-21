def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
    try:

        if prior_a < 0 or prior_a > 1 or prior_b < 0 or prior_b > 1 or conditional_b_given_a < 0 or conditional_b_given_a > 1:
            raise ValueError("Invalid probability values. Probabilities must be between 0 and 1.")


        probability_a_given_b = (conditional_b_given_a * prior_a) / prior_b
        return probability_a_given_b
    except ZeroDivisionError:
        return 0
    except ValueError as e:
        return str(e)


prior_a = 0.3
prior_b = 0.6
conditional_b_given_a = 0.8


result = bayes_theorem(prior_a, prior_b, conditional_b_given_a)
print( result)
