import streamlit as st
import random

# -----------------------
# Simple "database"
# -----------------------
if "users" not in st.session_state:
    # username -> password
    st.session_state.users = {}

# -----------------------
# Session state defaults
# -----------------------
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "current_view" not in st.session_state:
    st.session_state.current_view = "login"  # or "register" / "dashboard"


# -----------------------
# Helper functions
# -----------------------
def switch_view(view_name: str) -> None:
    """Update the current view shown to the user."""
    st.session_state.current_view = view_name


def register_user(username: str, password: str) -> str:
    """
    Attempt to register a new citizen.
    Returns an error message string, or empty string on success.
    """
    if not username:
        return "Username cannot be empty."

    if username in st.session_state.users:
        return "That username is already taken."

    if len(password) < 4:
        return "Password must be at least 4 characters."

    st.session_state.users[username] = password
    return ""  # success


def authenticate_user(username: str, password: str) -> bool:
    """Return True if the credentials are valid, False otherwise."""
    stored_pw = st.session_state.users.get(username)
    return stored_pw is not None and stored_pw == password


def logout() -> None:
    """Clear authentication-related state."""
    st.session_state.is_authenticated = False
    st.session_state.current_user = None
    switch_view("login")


# -----------------------
# UI components
# -----------------------
def show_header():
    st.title("Citizen Wellness Portal™")
    st.caption("Because The Algorithm cares about your holistic optimization.")


def show_sidebar():
    with st.sidebar:
        st.header("Navigation")
        if st.session_state.is_authenticated:
            st.write(f"Status: ✅ Logged in as **{st.session_state.current_user}**")
            if st.button("Dashboard"):
                switch_view("dashboard")
            if st.button("Logout"):
                logout()
        else:
            st.write("Status: ❌ Not authenticated")
            if st.button("Login"):
                switch_view("login")
            if st.button("Register"):
                switch_view("register")


def registration_view():
    st.subheader("New Citizen Registration")

    with st.form("registration_form"):
        username = st.text_input("Choose a username")
        password = st.text_input("Choose a password", type="password")
        submitted = st.form_submit_button("Register")

    if submitted:
        error = register_user(username, password)
        if error:
            st.error(error)
        else:
            st.success("Registration successful! Please log in.")
            switch_view("login")


def login_view():
    st.subheader("Authentication Portal")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log In")

    if submitted:
        if authenticate_user(username, password):
            st.session_state.is_authenticated = True
            st.session_state.current_user = username
            st.success("Access granted. Welcome, citizen.")
            switch_view("dashboard")
        else:
            st.error("Invalid credentials. The Algorithm is displeased.")


def dashboard_view():
    if not st.session_state.is_authenticated:
        st.warning("You must be logged in to view the dashboard.")
        switch_view("login")
        return

    st.subheader("Citizen Wellness Dashboard")

    username = st.session_state.current_user
    st.write(f"Welcome, **{username}**. Here are your wellness metrics:")

    # Mock metrics (random each time for fun)
    energy = random.randint(40, 100)
    focus = random.randint(30, 100)
    happiness = random.randint(20, 100)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Energy", f"{energy}%", "+3%")
    with col2:
        st.metric("Focus", f"{focus}%", "-1%")
    with col3:
        st.metric("Happiness", f"{happiness}%", "+7%")

    st.write("---")
    st.write("Remember: consistent hydration increases favor with The Algorithm.")


# -----------------------
# Main app
# -----------------------
def main():
    show_header()
    show_sidebar()

    view = st.session_state.current_view

    if view == "register":
        registration_view()
    elif view == "dashboard":
        dashboard_view()
    else:
        login_view()  # default


if __name__ == "__main__":
    main()