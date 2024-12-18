import streamlit as st

st.set_page_config(layout="wide")

# Set up session state for navigation and modals
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "show_modal" not in st.session_state:
    st.session_state.show_modal = False

# Inject CSS for styling
st.markdown("""
<style>
/* Overall background white */
.stApp {
    background: white !important;
}

/* Title styling */
h1 {
    color: #0077cc !important; /* Light blue title */
}

/* Sidebar buttons uniform width and light blue background */
.sidebar-button > button {
    width: 200px !important;
    background-color: #add8e6 !important; /* Light blue */
    color: #000 !important;
    font-weight: bold !important;
    margin-bottom: 10px !important;
    border: none !important;
}

/* Card styling */
.card-button > button {
    background: #ffffff !important; /* White card */
    border: 1px solid #ddd !important;
    border-radius: 4px !important;
    width: 100% !important;
    text-align: left !important;
    padding: 20px !important;
    margin-bottom: 20px !important;
    color: #000 !important;
    font-weight: normal !important;
    cursor: pointer;
    font-family: Arial, sans-serif;
}
.card-button > button:hover {
    background: #f0f0f0 !important; /* Light gray hover effect */
}
</style>
""", unsafe_allow_html=True)

def render_home():
    st.title("The Frontier MINDS Toolkit")

    # Fun
