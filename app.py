import streamlit as st
from calculator import calculate_progress
from sample_data import sample_data

st.title("📊 Grade Progress Tracker")

# 1️⃣ Set target grade from user input
target = st.number_input("Enter your target final grade (%):", min_value=0.0, max_value=100.0, value=90.0)

# 📥 Entering Target Grade Input 
st.subheader("📥 Enter Your Grade Info")

with st.form("grade_form"):
    category_names = []
    category_weights = []
    total_counts = []
    category_scores = []

    for i in range(3):  # allow 3 sections for now (Quiz, Exam, etc)
        st.markdown(f"### Category {i + 1}")

        name = st.text_input(f"Name (e.g., Quiz)", key=f"name_{i}")
        weight = st.number_input("Weight (%)", min_value=0.0, max_value=100.0, key=f"weight_{i}")
        total = st.number_input("Total Items", min_value=1, max_value=50, key=f"total_{i}")
        scores_text = st.text_input("Scores so far (comma-separated)", key=f"scores_{i}")

        category_names.append(name)
        category_weights.append(weight)
        total_counts.append(total)
        category_scores.append(scores_text)

    submitted = st.form_submit_button("📊 Calculate My Progress")
    
# Conerting to Data form after submission 
if submitted:
    data = []
    for i in range(3):
        if category_names[i].strip() == "":
            continue

        try:
            scores = [float(s.strip()) for s in category_scores[i].split(",") if s.strip() != ""]
        except ValueError:
            st.error(f"Invalid scores in Category {i + 1}. Please enter numbers only.")
            continue

        data.append({
            "name": category_names[i],
            "weight": category_weights[i],
            "scores": scores,
            "total_count": total_counts[i]
        })

    # Calculate and show result
    if data:
        result = calculate_progress(data, target)
        st.subheader("✅ Overall Progress")
        st.write(f"• Earned: {result['total_earned']}%")
        st.write(f"• Remaining: {result['total_remaining']}%")
        st.write(f"• Avg Needed to Hit Target: {result['avg_needed_for_target']}%")

        st.subheader("📂 Breakdown by Category")
        for cat in result["categories"]:
            st.markdown(f"**{cat['name']}**")
            st.write(f"• Earned: {cat['earned']}%")
            st.write(f"• Remaining: {cat['remaining']}%")
            st.markdown("---")


# 3️⃣ Run calculation
result = calculate_progress(sample_data, target)

# 4️⃣ Display results
st.subheader("Overall Progress")
st.write(f"✅ Earned: {result['total_earned']}%")
st.write(f"🕓 Remaining: {result['total_remaining']}%")
st.write(f"🎯 Needed Avg to Hit Target: {result['avg_needed_for_target']}%")

st.subheader("Breakdown by Category")
for category in result["categories"]:
    st.write(f"**{category['name']}**")
    st.write(f"• Earned: {category['earned']}%")
    st.write(f"• Remaining: {category['remaining']}%")
    st.markdown("---")

