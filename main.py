import os
import streamlit as st
import main_api

# Fetch the password from environment variable
password = st.secrets["general"]["STREAMLIT_PASSWORD"]

# Create a simple password authentication
def check_password():
    """Returns True if the user had the correct password."""
    st.session_state["password"] = st.text_input("Hasło", type="password")
    if st.session_state["password"] == password:
        return True
    elif st.session_state["password"]:
        st.error("Incorrect password")
        return False

if check_password():
    st.write("Ok, witam w API Acti")
    main_api.run()
else:
    st.warning("Wprowadź prawidłowe hasło")
