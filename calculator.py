def calculate_progress(data, target_grade):
    categories = []
    total_earned = 0
    total_remaining = 0

    for item in data:
        name = item["name"]
        weight = item["weight"]  # total weight of this category
        scores = item["scores"]  # list of percentages, like [75, 80]
        total_count = item["total_count"]  # total # of items (e.g., 10 quizzes)

        completed_count = len(scores)
        if completed_count > 0:
            avg_score = sum(scores) / completed_count
        else:
            avg_score = 0

        percent_completed = completed_count / total_count if total_count else 0
        earned_weight = (avg_score / 100) * percent_completed * weight
        remaining_weight = weight - (percent_completed * weight)

        categories.append({
            "name": name,
            "earned": round(earned_weight, 2),
            "remaining": round(remaining_weight, 2),
            "avg_needed_for_target": None  # optional, for future
        })

        total_earned += earned_weight
        total_remaining += remaining_weight

    if total_remaining > 0:
        avg_needed = (target_grade - total_earned) / (total_remaining / 100)
        avg_needed = round(avg_needed, 2)
    else:
        avg_needed = None

    return {
        "categories": categories,
        "total_earned": round(total_earned, 2),
        "total_remaining": round(total_remaining, 2),
        "avg_needed_for_target": avg_needed
    }
