def calculate_advertising_score(ratio):
    """
    Calculates the Advertising Score based on the given ratio.

    Parameters:
    ratio (float): The ratio of advertising expenses to revenue.

    Returns:
    float: The Advertising Score, between 0 and 100.
    """
    # Variabe 
    ideal_score = 100
    ideal_ratio = 0.2
    zero_score_ratio_1 = 0
    zero_score_ratio_2 = 0.5
    min_score = 0
    max_score = 100
    
    if ratio <= zero_score_ratio_1:
        return min_score
    elif ratio >= zero_score_ratio_2:
        return min_score
    elif ratio == ideal_ratio:
        return max_score
    elif zero_score_ratio_1 < ratio < ideal_ratio:
        # Score decreases slower as it approaches the ideal ratio of 0.2
        score = ((ratio - zero_score_ratio_1) / ideal_ratio)**0.5 * max_score
        return round(score, 2)
    elif ideal_ratio < ratio < zero_score_ratio_2:
        # Score decreases quicker as it approaches the maximum value of 0.5
        score = max_score - ((ratio - ideal_ratio) / (zero_score_ratio_2 - ideal_ratio ))**0.5  * max_score
        score = max(min_score, score)
        return round(score, 2)