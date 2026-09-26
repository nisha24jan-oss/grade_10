import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        max-width: 700px;
        margin: auto;
    }

    .title {
        font-size: 32px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0;
    }

    .subtitle {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .strength-box {
        background-color: #e9fbe9;
        padding: 20px;
        border-radius: 10px;
        margin-top: 15px;
    }

    .strength-title {
        color: #087f23;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .progress {
        height: 10px;
        background-color: #d1d5db;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 15px;
    }

    .progress-bar {
        height: 100%;
        background-color: #10b981;
        width: 100%;
        border-radius: 10px;
    }

    .check {
        color: #16a34a;
        font-size: 14px;
        margin: 7px 0;
    }

    .check span {
        margin-left: 8px;
        color: #475569;
    }
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    '<div class="title">🔐 Password Strength Checker</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Check how strong your password is</div>',
    unsafe_allow_html=True
)


# Password input
password = st.text_input(
    "Enter your password:",
    type="password",
    placeholder="Enter password"
)


# Check Strength button
if st.button("Check Strength", use_container_width=True):

    # Password conditions
    length_check = len(password) >= 8
    upper_check = any(char.isupper() for char in password)
    lower_check = any(char.islower() for char in password)
    number_check = any(char.isdigit() for char in password)
    special_check = any(char in "!@#$%^&*" for char in password)

    score = sum([
        length_check,
        upper_check,
        lower_check,
        number_check,
        special_check
    ])

    # Strength message
    if score == 5:
        strength = "Strong Password"
    elif score >= 3:
        strength = "Medium Password"
    else:
        strength = "Weak Password"

    # Display result
    if score == 5:
        st.markdown("""
        <div class="strength-box">
            <div class="strength-title">Strong Password</div>

            <div class="progress">
                <div class="progress-bar"></div>
            </div>

            <div class="check">✔
                <span>At least 8 characters</span>
            </div>

            <div class="check">✔
                <span>Contains uppercase letter</span>
            </div>

            <div class="check">✔
                <span>Contains lowercase letter</span>
            </div>

            <div class="check">✔
                <span>Contains a number</span>
            </div>

            <div class="check">✔
                <span>Contains a special character</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning(f"⚠️ {strength}")

        st.write("Password requirements:")

        st.write(
            "✅ At least 8 characters"
            if length_check else
            "❌ At least 8 characters"
        )

        st.write(
            "✅ Contains uppercase letter"
            if upper_check else
            "❌ Contains uppercase letter"
        )

        st.write(
            "✅ Contains lowercase letter"
            if lower_check else
            "❌ Contains lowercase letter"
        )

        st.write(
            "✅ Contains a number"
            if number_check else
            "❌ Contains a number"
        )

        st.write(
            "✅ Contains a special character"
            if special_check else
            "❌ Contains a special character"
        )