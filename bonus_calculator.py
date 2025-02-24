import streamlit as st
import streamlit_authenticator as stauth

# Create user credentials
credentials = {
    "usernames": {
        "john_doe": {"name": "John Doe", "password": "password123"},
        "jane_smith": {"name": "Jane Smith", "password": "securepass"}
    }
}

# Create an authenticator object
authenticator = stauth.Authenticate(credentials, "app_login", "abcdef", cookie_expiry_days=1)

# Login widget
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f"Welcome, {name}!")
    authenticator.logout("Logout", "sidebar")

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
    st.warning("Please enter valid credentials to access the app.")
