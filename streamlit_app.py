import streamlit as st

st.set_page_config(layout="wide")

# Sidebar navigation
st.sidebar.markdown("**Home**")
st.sidebar.markdown("Industry")
st.sidebar.markdown("Function")
st.sidebar.markdown("Region")
st.sidebar.markdown("KPI")

# Main header
st.title("The Frontier MINDS Toolkit")

# Search input
default_query = "Show me the best AI applications on customer satisfaction in Consumers industry"
query = st.text_input("", value=default_query)

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

# Render two cards as in the mockup
render_card("Company name", "+x% customer retention", "10k daily active users")
render_card("Company name", "+x% customer retention", "10k daily active users")

