"""The relation between the ratio and score is non-linear. It is a piecewise function that behaves differently in different ranges of the ratio. In the range 0.1 <= ratio <= 0.5, the relation is non-linear and increasing. In the range ratio < 0.1 and ratio > 0.5, the relation is linear and decreasing"""

def calculate_cogs_score(ratio):
    # Set threshold ratio and threshold score
    
    threshold_ratio = 0.5
    threshold_score = 30
    zero_score_ratio = 0.65
    ideal_ratio =  0.1
    max_score = 100
    min_score = 0
    
    # If ratio is greater than or equal to 0.65, return 0
    if ratio >= zero_score_ratio:
        return min_score
    # If ratio is less than or equal to 0.1, return 100
    elif ratio <= ideal_ratio:
        return max_score
    # If ratio is greater than or equal to threshold ratio (0.5), calculate score based on linear equation
    elif ratio >= threshold_ratio:
        # Calculate score using linear equation and round to the nearest integer
        score = threshold_score * (1 - (ratio - threshold_ratio) / (1 - threshold_ratio))**12
        return (score)
    # If ratio is less than threshold ratio (0.5), calculate score based on non-linear equation
    else:
        # Scale the ratio to the range 0-1 and calculate score using non-linear equation
        #ratio_scaled = (threshold_ratio - ratio) / (threshold_ratio - ideal_ratio)
        score = threshold_score + ((threshold_ratio - ratio) / (threshold_ratio - ideal_ratio))**0.7 * (max_score - threshold_score)
        return (score)