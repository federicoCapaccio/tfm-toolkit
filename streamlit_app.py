import streamlit as st

st.set_page_config(layout="wide")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Define functions to render different pages
def render_home():
    st.title("The Frontier MINDS Toolkit")
    default_query = "Show me the best AI applications on customer satisfaction in Consumers industry"
    st.text_input("", value=default_query)

    def render_card(company_name, impact, scale):
        card_html = f"""
        <div style="background:#fff;padding:20px;margin-bottom:20px;box-sizing:border-box;border-radius:4px;display:flex;justify-content:space-between;align-items:center;border:1px solid #ddd;">
          <div style="display:flex;flex-direction:row;align-items:center;">
            <div style="font-weight:bold;margin-right:40px;">{company_name}</div>
            <div style="margin-right:40px;">
              <span style="color:#0070f3;font-weight:bold;margin-right:5px;">Impact Achieved</span>
              <span>{impact}</span>
            </div>
            <div style="margin-right:40px;">
              <span style="color:#0070f3;font-weight:bold;margin-right:5px;">Scale</span>
              <span>{scale}</span>
            </div>
            <div>--- ---</div>
          </div>
          <div style="color:#0070f3;cursor:pointer;">Explore more &rarr;</div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

    # Render two sample cards
    render_card("Company name", "+x% customer retention", "10k daily active users")
    render_card("Company name", "+x% customer retention", "10k daily active users")

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
if st.sidebar.button("Home"):
    st.session_state.page = "Home"
if st.sidebar.button("Industry"):
    st.session_state.page = "Industry"
if st.sidebar.button("Function"):
    st.session_state.page = "Function"
if st.sidebar.button("Region"):
    st.session_state.page = "Region"
if st.sidebar.button("KPI"):
    st.session_state.page = "KPI"

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
