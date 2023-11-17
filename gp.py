import numpy as np
import matplotlib.pyplot as plt
def calculate_gp_score(ratio):
    """
    Calculates the GP Score based on the given ratio.

    Parameters:
    ratio (float): The ratio of the GP to the income.

    Returns:
    float: The GP Score, between 0 and 100.
    """
    # Variables
    threshold_ratio = 0.188
    threshold_score = 70
    max_ratio = 0.4
    max_score = 100
    zero_ratio = 0.075
    zero_score = 0
    min_score = 0
    
    # Calculate the score using a logarithmic equation that passes through the given points
    if ratio <= zero_ratio:
        score = zero_score
    elif ratio <= threshold_ratio:
        score = max_score * (np.log10(ratio/zero_ratio) / np.log10(threshold_ratio/zero_ratio)**0.6)
    elif ratio <= max_ratio:
        score = ((ratio - threshold_ratio) / (max_ratio - threshold_ratio))**0.5 * (max_score - threshold_score) + threshold_score
    else:
        score = 100
    
    # Ensure score is within range [0, 100]
    score = max(min_score, min(max_score, score))
    
    return (score)
