import numpy as np
import matplotlib.pyplot as plt

def calculate_rent_score(ratio):
    """
    Calculates the Rent Score based on the given ratio.

    Parameters:
    ratio (float): The ratio of the rent to the income.

    Returns:
    float: The Rent Score, between 0 and 100.
    """
    # Variables
    threshold_ratio = 0.04
    threshold_score = 30
    zero_score_ratio = 0.1
    ideal_ratio =  0
    max_score = 100
    min_score = 0
    
    if ratio <= ideal_ratio:
        return max_score
    elif ratio >= zero_score_ratio:
        return min_score
    elif ideal_ratio < ratio < threshold_ratio:
        score = max_score - ((ratio - ideal_ratio) / threshold_ratio)**1.5 * (max_score - threshold_score)
        return int(score)
    elif threshold_ratio <= ratio <= zero_score_ratio:
        score = threshold_score - ((ratio - threshold_ratio) / (zero_score_ratio - threshold_ratio))**.5  * threshold_score
        return int(score)
    else:
        score = (np.log10(ratio/ideal_ratio) / np.log10(zero_score_ratio/ideal_ratio)) * (min_score - max_score) + max_score
        return int(score)
