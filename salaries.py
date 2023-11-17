import numpy

def calculate_salary_score(ratio):
    # Set ideal ratio and ideal score
    ideal_ratio = 0.3
    ideal_score = 100
    zero_score_ratio_1 = 0.100
    zero_score_ratio_2 = 0.500
    min_score = 0
    max_score = 100

    if ratio <= zero_score_ratio_1 or ratio >= zero_score_ratio_2:
        return min_score
    elif ratio == ideal_ratio:
        return ideal_score
    elif ratio < ideal_ratio:
        # Calculate score using a smooth curve from 0.1 to 0.3
        score = ideal_score * ((ratio - zero_score_ratio_1) / (ideal_ratio - zero_score_ratio_1)) ** 3
        return numpy.round(score,2)
    else:
        # Calculate score using a smooth curve from 0.3 to 0.5
        score = ideal_score * ((zero_score_ratio_2 - ratio) / (zero_score_ratio_2 - ideal_ratio)) ** 3
        return numpy.round(score, 2)