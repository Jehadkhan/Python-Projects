def calculate_op_expenses_score(ratio):
    """
    Calculates the Op Expenses Score based on the given ratio.

    Parameters:
    ratio (float): A float value between 0 and 1 representing the ratio.

    Returns:
    score (float): A float value between 0 and 100 representing the Op Expenses Score.

    """
    # Variable
    threshold_ratio = 0.64
    threshold_score = 30
    ideal_ratio = 0.2
    zero_score_ratio = 0.8
    max_score = 100
    
    # Logic
    if ratio >= zero_score_ratio:
        return 0
    elif ratio <= ideal_ratio:
        return max_score
    else:
        if ratio <= threshold_ratio:
            score = max_score - ((ratio - ideal_ratio) / (threshold_ratio - ideal_ratio)) ** 2 * 70
        else:
            score = threshold_score - ((ratio - threshold_ratio) / (zero_score_ratio - threshold_ratio)) ** 0.85 * 30
        return round(max(0, min(score, max_score)), 2)