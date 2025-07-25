def generate_advice(result):
    advice = []

    total_remaining = result["total_remaining"]
    avg_needed = result["avg_needed_for_target"]

    # 1. Overall pressure
    if total_remaining > 70:
        advice.append("⚠️ You still have over 70% of your grade left. Plan carefully.")
    elif total_remaining < 30:
        advice.append("✅ You're almost done! Stay steady to reach your goal.")

    # 2. Needed average to hit goal
    if avg_needed > 95:
        advice.append("🚨 You must work your ass off — you need to average above 95% going forward.")
    elif avg_needed > 90:
        advice.append("🎯 Focus mode: Aim for 90%+ on all remaining tasks.")
    elif avg_needed < 80:
        advice.append("🟢 You're on track — just maintain your performance.")

    # 3. Category-specific advice
    for cat in result["categories"]:
        name = cat["name"]
        earned = cat["earned"]
        remaining = cat["remaining"]

        # Skip categories with no remaining weight
        if remaining == 0:
            continue

        # Priority push for heavy categories
        if remaining >= 20:
            if earned < remaining * 0.5:
                advice.append(f"🔥 Your {name} score is low and it's heavily weighted. Prioritize this.")
            else:
                advice.append(f"📌 {name} is still a major part of your grade. Stay sharp.")

        # Light category but low performance
        elif earned < remaining * 0.3:
            advice.append(f"🔍 Improve your {name} score — it's small but pulling you down.")

        # Full points already earned
        if earned > 0 and remaining == 0:
            advice.append(f"✅ You've completed all your {name} tasks. Good job.")

    return advice
