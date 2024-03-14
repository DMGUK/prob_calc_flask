def adding_formula(prob_A, prob_B):
    result = prob_A + prob_B - (prob_A * prob_B)
    return result

def multiplying_formula(prob_A, prob_B):
    result = prob_A * prob_B
    return result

def full_probability_formula(conditional_probabilities, prior_probabilities):
    total_probability = 0
    for cond_prob, prior_prob in zip(conditional_probabilities, prior_probabilities):
        total_probability += cond_prob * prior_prob
    return total_probability

def bayes_formula(prob_A, prob_B, prob_BA):
    return prob_A * prob_BA / prob_B

def single_event_formula(probabilities):
    complementary_probability = 1
    for p in probabilities:
        complementary_probability *= (1 - p)
    return 1 - complementary_probability
