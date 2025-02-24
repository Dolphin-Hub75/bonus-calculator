
import streamlit as st
import streamlit_authenticator as stauth
import bcrypt

# Create user credentials with hashed passwords
credentials = {
    "usernames": {
        "alan_bailey": {
            "name": "Alan Bailey",
            "password": "$2b$12$jN5ADtD.xt0kVb3/cXWzo.FHjyfUiAaBOgl.5gF5tUyhX8k./OvNy",  # Hashed password
            "email": "bailey.alan@gmail.com"
        },
        "jane_smith": {
            "name": "Jane Smith",
            "password": "$2b$12$Hlh7vlD8FZezhAaR.R/I/.3qy8OxFe69XwYuMoYKd946IqI3Fuycq",  # Hashed password
            "email": "janesmith@example.com"
        }
    }
}

# Create an authenticator object
authenticator = stauth.Authenticate(credentials, "app_login", "abcdef", cookie_expiry_days=1)

# Login widget
authentication_status = authenticator.login()
st.write(f"Auth Status: {authentication_status}")  # Debugging output

if authentication_status:
    st.success("Login successful!")
    authenticator.logout("Logout", "sidebar")

    # Bonus Calculator Logic
    def calculate_bonus(completed_jobs, days_worked):
        job_thresholds = {
            5: (34, 34),
            4: (27, 27),
            3: (21, 21),
            2: (14, 14),
            1: (7, 7)
        }

        if days_worked not in job_thresholds:
            return "Invalid number of days worked. Please enter a value between 1 and 5."

        base_jobs, base_bonus = job_thresholds[days_worked]

        if completed_jobs < base_jobs:
            return f"No bonus. {completed_jobs} jobs completed, {base_jobs} required."

        bonus = base_bonus if completed_jobs >= base_jobs else 0

        extra_jobs = max(completed_jobs - base_jobs, 0)

        for i in range(extra_jobs):
            if base_jobs + i + 1 <= base_jobs + 7:
                bonus += 4 + i
            else:
                bonus += 10

        return f"Total bonus: £{bonus:.2f} for {completed_jobs} completed jobs."

    st.title("Engineer Bonus Calculator")
    completed_jobs = st.number_input("Enter the number of completed jobs:", min_value=0, step=1)
    days_worked = st.number_input("Enter the number of days worked (1-5):", min_value=1, max_value=5, step=1)

    if st.button("Calculate Bonus"):
        result = calculate_bonus(completed_jobs, days_worked)
        st.write(result)

else:
    st.warning("Please enter your credentials to continue.")
