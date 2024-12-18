import streamlit as st

st.set_page_config(layout="wide")

# Initialize state
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

/* Sidebar buttons uniform width and light blue background */
.sidebar-button > button {
    width: 200px !important;
    background-color: #add8e6 !important;
    color: #000 !important;
    font-weight: bold !important;
    margin-bottom: 10px !important;
    border: none !important;
}

/* Card styling */
.card-button > button {
    background: #fff !important;
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
    background: #f0f0f0 !important;
}
</style>
""", unsafe_allow_html=True)

def render_home():
    # Use st.markdown to set the title to light blue
    st.markdown("<h1 style='color: #add8e6; font-family: Arial, sans-serif;'>The Frontier MINDS Toolkit</h1>", unsafe_allow_html=True)
    default_query = "Show me the best AI applications on customer satisfaction in Consumers industry"
    st.text_input("", value=default_query)

    # Function to render a card as a clickable button
    def render_card(company_name, impact, scale, key):
        # Label for the button
        label = f"{company_name}     Impact Achieved: {impact}     Scale: {scale}                  Explore more →"
        
        # Create a container for card-button to apply CSS
        with st.container():
            st.markdown('<div class="card-button">', unsafe_allow_html=True)
            if st.button(label, key=key):
                st.session_state.show_modal = True
            st.markdown('</div>', unsafe_allow_html=True)

    # Render two sample cards
    render_card("Company name", "+x% customer retention", "10k daily active users", "card1")
    render_card("Company name", "+x% customer retention", "10k daily active users", "card2")

    # If a card was clicked, show the modal
    if st.session_state.show_modal:
        with st.modal("Details"):
            st.write("explore details here")
            if st.button("Close"):
                st.session_state.show_modal = False

def render_industry():
    # Just a title and blank page
    st.markdown("<h1 style='color: #add8e6; font-family: Arial, sans-serif;'>Industry Page</h1>", unsafe_allow_html=True)

def render_function():
    st.markdown("<h1 style='color: #add8e6; font-family: Arial, sans-serif;'>Function Page</h1>", unsafe_allow_html=True)

def render_region():
    st.markdown("<h1 style='color: #add8e6; font-family: Arial, sans-serif;'>Region Page</h1>", unsafe_allow_html=True)

def render_kpi():
    st.markdown("<h1 style='color: #add8e6; font-family: Arial, sans-serif;'>KPI Page</h1>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("### Navigation")
with st.sidebar.container():
    st.markdown('<div class="sidebar-button">', unsafe_allow_html=True)
    if st.button("Home"):
        st.session_state.page = "Home"
    if st.button("Industry"):
        st.session_state.page = "Industry"
    if st.button("Function"):
        st.session_state.page = "Function"
    if st.button("Region"):
        st.session_state.page = "Region"
    if st.button("KPI"):
        st.session_state.page = "KPI"
    st.markdown('</div>', unsafe_allow_html=True)

# Render the selected page
if st.session_state.page == "Home":
    render_home()
elif st.session_state.page == "Industry":
    render_industry()
elif st.session_state.page == "Function":
    render_function()
elif st.session_state.page == "Region":
    render_region()
elif st.session_state.page == "KPI":
    render_kpi()
