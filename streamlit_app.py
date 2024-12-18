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

/* Sidebar buttons uniform width and light blue background */
.sidebar-button > button {
    width: 200px !important;
    background-color: #add8e6 !important;
    color: #000 !important;
    font-weight: bold !important;
    margin-bottom: 10px !important;
    border: none !important;
}

/* Card styling (we'll use a button and style it like a card) */
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
.card-content {
    display: flex; 
    flex-direction: row; 
    align-items: center;
    justify-content: space-between;
}
.company-info {
    display: flex; 
    flex-direction: row; 
    align-items: center;
}
.company-info > div {
    margin-right: 40px;
}
.explore {
    color: #0070f3;
    font-weight: bold;
    float: right;
}
.impact-label {
    color: #0070f3;
    font-weight: bold;
    margin-right: 5px;
}
</style>
""", unsafe_allow_html=True)

def render_home():
    st.title("The Frontier MINDS Toolkit")
    default_query = "Show me the best AI applications on customer satisfaction in Consumers industry"
    st.text_input("", value=default_query)

    # Function to render a "card" as a button
    def render_card(company_name, impact, scale, key):
        # Create a label that visually looks like a card.
        # We'll use simple spacing. The HTML won't render in a button label, so we rely on spacing.
        # We can break lines using "\n" and spaces to simulate layout.
        # Instead, we'll present the content inline.
        # The styling from CSS above will shape the button.
        
        # We'll simulate the layout with a single line of text.
        label = f"{company_name}     Impact Achieved: {impact}     Scale: {scale}                  Explore more →"
        
        # Clicking this button sets show_modal to True
        if st.button(label, key=key):
            st.session_state.show_modal = True

    # Render two cards
    render_card("Company name", "+x% customer retention", "10k daily active users", "card1")
    render_card("Company name", "+x% customer retention", "10k daily active users", "card2")

    # If a card was clicked, show the modal
    if st.session_state.show_modal:
        with st.modal("Details"):
            st.write("explore details here")
            # Add a button to close the modal
            if st.button("Close"):
                st.session_state.show_modal = False

def render_industry():
    st.title("Industry Page")

def render_function():
    st.title("Function Page")

def render_region():
    st.title("Region Page")

def render_kpi():
    st.title("KPI Page")

# Sidebar navigation
st.sidebar.markdown("### Navigation")
with st.sidebar.container():
    with st.container():
        # Wrap buttons in a container with a class for uniform styling
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
