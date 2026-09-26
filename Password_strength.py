import streamlit as st

st.title("🔐 Password Strength Checker")

password = st.text_input(
    "Enter your password:",
    type="password"
)

if password:
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in "!@#$%^&*" for char in password):
        score += 1

    if score <= 2:
        st.error("🔴 Weak Password")
    elif score <= 4:
        st.warning("🟡 Medium Password")
    else:
        st.success("🟢 Strong Password")