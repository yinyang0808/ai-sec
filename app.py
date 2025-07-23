import streamlit as st

st.title("📚 AI Secretary Demo")

st.write("This is a basic test to see if your Streamlit app works!")

# Simple input fields
name = st.text_input("Enter your name:")
grade = st.number_input("Enter your current grade (%):", min_value=0.0, max_value=100.0)

if st.button("Submit"):
    st.success(f"Hi {name}! Your current grade is {grade}%. You're all set.")
