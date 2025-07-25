import streamlit as st
from calculator import calculate_progress
from sample_data import sample_data

# (Optional) You can move sample data to a new file if you want (see #4 below)

st.title("📊 Grade Progress Tracker")

# 1️⃣ Set target grade from user input
target = st.number_input("Enter your target final grade (%):", min_value=0.0, max_value=100.0, value=90.0)

# 2️⃣ For now: test with sample data
sample_data = [...]  # from earlier or imported

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

