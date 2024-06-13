import streamlit as st

st.set_page_config(page_title="ExamSave Student Page", page_icon="📄")

# Function to read the variable from a file
def read_variable():
    try:
        with open('variable.txt', 'r') as file:
            return file.read().strip()  # Use strip() to remove any extra whitespace
    except FileNotFoundError:
        return 'No variable set'

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'variable' not in st.session_state:
    st.session_state.variable = ''
if 'target_variable' not in st.session_state:
    st.session_state.target_variable = read_variable()

# Function to navigate to a different page
def navigate_to(page):
    st.session_state.page = page

# Login page
def login_page():
    st.title("Login to Examination")
    
    # Use password input to avoid markdown interpretation
    password = st.text_input("Enter password to access examination", type="password")
    if st.button("Submit"):
        st.session_state.variable = password.strip()  # Use strip() to remove any extra whitespace
        if st.session_state.variable == st.session_state.target_variable:
            navigate_to('exam')
        else:
            st.error("Incorrect password, try again.")

# Exam page
def exam_page():
    st.title("Examination")

# Page switcher
if st.session_state.page == 'login':
    login_page()
elif st.session_state.page == 'exam':
    exam_page()